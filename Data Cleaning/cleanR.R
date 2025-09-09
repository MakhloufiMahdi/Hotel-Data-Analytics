install.packages("writexl")
install.packages("writexl")
library(tidyverse)
library(lubridate)
library(writexl)

hotel_bookings <- read.csv("HOTELDATA.csv", stringsAsFactors = FALSE)

str(hotel_bookings)
summary(hotel_bookings)

colSums(is.na(hotel_bookings))

hotel_bookings <- hotel_bookings %>%
  mutate(children = ifelse(is.na(children), 0, children),
         babies = ifelse(is.na(babies), 0, babies))


hotel_bookings <- hotel_bookings %>%
  filter(!is.na(country)) 

hotel_bookings <- hotel_bookings %>%
  mutate(company = ifelse(is.na(company) | company == "NULL", "None", company),
         agent = ifelse(is.na(agent) | agent == "NULL", "None", agent))

hotel_bookings <- hotel_bookings %>%
  mutate(reservation_status_date = ymd(reservation_status_date))

categorical_cols <- c("hotel", "is_canceled", "arrival_date_month", "meal", 
                      "country", "market_segment", "distribution_channel",
                      "is_repeated_guest", "reserved_room_type", 
                      "assigned_room_type", "deposit_type", "customer_type",
                      "reservation_status")

hotel_bookings <- hotel_bookings %>%
  mutate(across(all_of(categorical_cols), as.factor))

hotel_bookings <- hotel_bookings %>%
  mutate(is_canceled = as.logical(as.integer(as.character(is_canceled))),
         is_repeated_guest = as.logical(as.integer(as.character(is_repeated_guest))))


hotel_bookings <- hotel_bookings %>%
  filter(lead_time >= 0)

hotel_bookings <- hotel_bookings %>%
  filter(adults > 0)

hotel_bookings <- hotel_bookings %>%
  filter(adr >= 0)


hotel_bookings <- hotel_bookings %>%
  mutate(total_nights = stays_in_weekend_nights + stays_in_week_nights,
         total_guests = adults + children + babies)


hotel_bookings <- hotel_bookings %>%
  mutate(season = case_when(
    arrival_date_month %in% c("December", "January", "February") ~ "Winter",
    arrival_date_month %in% c("March", "April", "May") ~ "Spring",
    arrival_date_month %in% c("June", "July", "August") ~ "Summer",
    arrival_date_month %in% c("September", "October", "November") ~ "Fall",
    TRUE ~ "Unknown"
  ))


hotel_bookings <- hotel_bookings %>%
  distinct()

colSums(is.na(hotel_bookings))

summary(hotel_bookings)

write_xlsx(hotel_bookings, "hotel_bookings_clean2.xlsx")
