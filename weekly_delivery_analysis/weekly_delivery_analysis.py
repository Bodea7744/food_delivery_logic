# Weekly delivery analysis

# Input section
deliveries_monday = int(input("Enter the number of deliveries for Monday:"))
deliveries_tuesday = int(input("Enter the number of deliveries for Tuesday:"))
deliveries_wednesday = int(input("Enter the number of deliveries for Wednesday:"))
deliveries_thursday = int(input("Enter the number of deliveries for Thursday:"))
deliveries_friday = int(input("Enter the number of deliveries for Friday:"))
deliveries_saturday = int(input("Enter the number of deliveries for Saturday:"))
deliveries_sunday = int(input("Enter the number of deliveries for Sunday:"))

# Calculating the total number of deliveries
total_deliveries = ( deliveries_monday + deliveries_tuesday + deliveries_wednesday + deliveries_thursday + deliveries_friday + deliveries_saturday + deliveries_sunday )
working_days_deliveries = ( deliveries_monday + deliveries_tuesday + deliveries_wednesday + deliveries_thursday + deliveries_friday )
weekend_deliveries = deliveries_saturday + deliveries_sunday

# Checking conditions as per the requirements
sunday_more_than_saturday = deliveries_sunday > deliveries_saturday
working_vs_weekend = working_days_deliveries > weekend_deliveries
successful_week = total_deliveries > 1000 or weekend_deliveries > 500

# Displaying the results
print(f"Total number of deliveries during the week: {total_deliveries}")
print(f"Number of deliveries on working days: {working_days_deliveries}")
print(f"Number of deliveries during the weekend: {weekend_deliveries}")
print(f"Sunday had more deliveries than Saturday: {sunday_more_than_saturday}")
print(f"Working days had more deliveries than the weekend: {working_vs_weekend}")
print(f"The week is considered successful: {successful_week}")