## Top Clients 

All Top 10 clients have only one booking but with huge amounts (e.g., €7,590, €6,630, €6,300).
Lead time often high (126 days, 113 days, 378 days).
These clients are very premium → likely families or groups booking far in advance for long stays.
But: no recurrence (none booked more than once).
The hotel thus attracts “big-ticket” occasional clients but does not retain them.
Recommendation:
Implement a VIP or premium loyalty program to encourage these clients to return.
Segment these profiles (long stays, high budget, high lead time) → specific targeting via email marketing.

## Correlation ADR vs Lead Time and Nights

Resort Hotel – Room B = strong correlation (0.79) → the higher the price, the earlier clients book and the longer they stay.
Resort Hotel – Rooms A, C, F, H = moderate correlations (0.14–0.24).
City Hotel – Rooms A, F, D = near-zero or negative correlations.
At the Resort Hotel, the price ↔ client behavior relationship is clear: the most expensive rooms attract organized and planned clients.
At the City Hotel, price doesn’t really influence length of stay or booking anticipation → logical, as clients are mostly business or short-stay travelers.
Recommendation:
Resort Hotel: implement dynamic pricing strategy (closer to date → higher price).
City Hotel: focus on volume and occupancy rather than anticipation → last-minute campaigns.

## Simple Forecast (Cumulative Bookings)
Steady growth: 1,672 bookings (2015–07) → 87,230 cumulative bookings (2017–08).
Average increase: +3,000 to +4,500 bookings per month.
Trend is strongly upward, proving demand is growing.
The hotel should plan for additional staff, rooms, and resources.
Cumulative bookings show ~+40,000 bookings per year → big opportunity but also risk of saturation.
 Recommendation:
Adjust capacity (more rooms, better schedule management).
Prepare a more advanced forecast (ARIMA or ML models) to predict the next season.

## Cancellations by Hotel, Channel, and Deposit Type
TA/TO + Non-Refund = very high cancellation rate (99% City Hotel, 84% Resort).
Direct + No Deposit = low cancellation rate (≈13% Resort, 12% City).
Corporate + No Deposit = even lower (≈9%).
Contrary to expectations, Non-Refund bookings don’t reduce cancellations → they are actually massive via TA/TO.
Direct or corporate bookings are the most stable (loyalty + less volatility).
OTAs (TA/TO) bring volume but also huge risk → destabilize net revenue (many no-shows and cancellations).
 Recommendation:
Reduce dependency on OTAs or apply stricter conditions.
Promote direct channels (website, loyalty, corporate deals).

## Lead Time (Booking Anticipation) by Month
Summer (July–August 2016–2017): lead time >100 days, with over 70% of bookings made 1 month in advance.
Winter (January–February 2016–2017): lead time drops to 22–45 days, with only 20–40% of bookings made in advance.
Booking is highly seasonal:
Summer = very early bookings (planned family vacations).
Winter = last-minute bookings (short stays, business or city trips).
High anticipation in summer allows dynamic pricing: closer to date → higher prices.
In low season, strategy should differ: last-minute offers, OTA discounts (Booking, Expedia), local campaigns.
 Recommendation:
Implement yield management → increase ADR for July–August, offer last-minute promotions in winter.

## Revenue by Hotel and Room Type (Relative Market Share)
City Hotel – Room A = 63% of total revenue
Resort Hotel – Room A = 44% of total revenue
Other rooms like C or B represent <1% of revenue.

Revenue is heavily concentrated on one or two room categories (e.g., City Hotel → Room A, Resort Hotel → Rooms A and D).
This means pricing strategy depends on a small number of room types → risky (if demand drops for these rooms → big impact).
Marginal rooms (B, C, L…) contribute almost nothing → they could either:

be repositioned (bundled with meals or promotions),
renovated if outdated,
or removed from inventory to reduce fixed costs.
Recommendation: Strengthen sales on minor categories to reduce dependency.
