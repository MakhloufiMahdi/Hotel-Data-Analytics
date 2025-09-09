import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.metrics import confusion_matrix, classification_report, roc_auc_score, roc_curve
import matplotlib.pyplot as plt


hotel = pd.read_csv("hotel_bookings.csv")
hotel["is_canceled"] = hotel["is_canceled"].astype(int)
hotel = hotel.dropna()


leak_cols = ['reservation_status', 'reservation_status_date', 'assigned_room_type']
hotel = hotel.drop(columns=[col for col in leak_cols if col in hotel.columns])

hotel['total_guests'] = hotel['adults'] + hotel['children'] + hotel['babies']
hotel['stay_duration'] = hotel['stays_in_weekend_nights'] + hotel['stays_in_week_nights']
hotel['is_family'] = np.where(hotel['children'] + hotel['babies'] > 0, 1, 0)


X = hotel.drop("is_canceled", axis=1)
y = hotel["is_canceled"]


num_cols = X.select_dtypes(include=['int64','float64']).columns.tolist()
cat_cols = X.select_dtypes(include=['object']).columns.tolist()


preprocessor = ColumnTransformer([
    ('num', StandardScaler(), num_cols),
    ('cat', OneHotEncoder(handle_unknown='ignore'), cat_cols)
])


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

log_pipe = Pipeline([
    ('prep', preprocessor),
    ('clf', LogisticRegression(max_iter=1000, class_weight='balanced'))
])
log_pipe.fit(X_train, y_train)

rf_pipe = Pipeline([
    ('prep', preprocessor),
    ('clf', RandomForestClassifier(n_estimators=200, max_depth=15, class_weight='balanced', random_state=42))
])
rf_pipe.fit(X_train, y_train)


xgb_pipe = Pipeline([
    ('prep', preprocessor),
    ('clf', XGBClassifier(use_label_encoder=False, eval_metric='logloss', random_state=42))
])

param_dist = {
    'clf__n_estimators': [200, 300],
    'clf__max_depth': [5, 7, 9],
    'clf__learning_rate': [0.01, 0.05, 0.1],
    'clf__subsample': [0.8, 1.0],
    'clf__colsample_bytree': [0.7, 0.8, 1.0],
    'clf__scale_pos_weight': [y.value_counts()[0]/y.value_counts()[1]]
}

search = RandomizedSearchCV(
    xgb_pipe,
    param_distributions=param_dist,
    n_iter=10,
    scoring='roc_auc',
    cv=3,
    verbose=1,
    random_state=42,
    n_jobs=-1
)

search.fit(X_train, y_train)
best_xgb = search.best_estimator_
print("\nMeilleurs paramètres XGBoost trouvés :")
print(search.best_params_)


def evaluate_model(model, X_test, y_test, name):
    y_pred = model.predict(X_test)
    y_proba = model.predict_proba(X_test)[:,1]
    print(f"\n--- {name} ---")
    print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
    print("Classification Report:\n", classification_report(y_test, y_pred))
    auc = roc_auc_score(y_test, y_proba)
    print(f"AUC: {auc:.3f}")
    return y_proba, auc

y_proba_log, auc_log = evaluate_model(log_pipe, X_test, y_test, "Logistic Regression")
y_proba_rf, auc_rf   = evaluate_model(rf_pipe, X_test, y_test, "Random Forest")
y_proba_xgb, auc_xgb = evaluate_model(best_xgb, X_test, y_test, "XGBoost Optimisé")


plt.figure(figsize=(8,6))
for y_proba, auc, name in zip([y_proba_log, y_proba_rf, y_proba_xgb],
                               [auc_log, auc_rf, auc_xgb],
                               ["Logistic", "RF", "XGB"]):
    fpr, tpr, _ = roc_curve(y_test, y_proba)
    plt.plot(fpr, tpr, label=f"{name} (AUC={auc:.3f})")
plt.plot([0,1],[0,1],'k--')
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve comparée")
plt.legend()
plt.show()

importances = best_xgb.named_steps['clf'].feature_importances_
ohe_features = best_xgb.named_steps['prep'].transformers_[1][1].get_feature_names_out(cat_cols)
all_features = num_cols + list(ohe_features)
feat_importances = pd.Series(importances, index=all_features)
feat_importances.nlargest(15).plot(kind='barh', figsize=(10,6), title="Top 15 features importantes")
plt.show()

