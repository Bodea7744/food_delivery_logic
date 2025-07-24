# Advanced weekly delivery analysis

# Input section
deliveries_monday = int(input("Enter the number of deliveries on Monday: "))
deliveries_tuesday = int(input("Enter the number of deliveries on Tuesday: "))
deliveries_wednesday = int(input("Enter the number of deliveries on Wednesday: "))
deliveries_thursday = int(input("Enter the number of deliveries on Thursday: "))
deliveries_friday = int(input("Enter the number of deliveries on Friday: "))
deliveries_saturday = int(input("Enter the number of deliveries on Saturday: "))
deliveries_sunday = int(input("Enter the number of deliveries on Sunday: "))

# Total deliveries calculation
deliveries_workdays = ( deliveries_monday + deliveries_tuesday + deliveries_wednesday + deliveries_thursday + deliveries_friday )
deliveries_weekend = deliveries_saturday + deliveries_sunday
total_deliveries = deliveries_workdays + deliveries_weekend

# Display results
print(f"Total number of deliveries for the whole week: {total_deliveries}")
print(f"Total number of deliveries on workdays: {deliveries_workdays}")
print(f"Total number of deliveries on the weekend: {deliveries_weekend}")

# Compare Saturday vs Sunday using inline if
print("Sunday had more deliveries than Saturday.") if deliveries_sunday > deliveries_saturday else print("Saturday had more deliveries than Sunday.")

# Compare workdays vs weekend
if deliveries_workdays > deliveries_weekend:
    print("Workdays had more deliveries than the weekend.")
else:
    print("The weekend had more deliveries than workdays.")

# Compare weekend days using logical operators
if deliveries_saturday > 100 and deliveries_sunday > 100:
    print("Both weekend days had more than 100 deliveries.")
elif deliveries_saturday > 100 or deliveries_sunday > 100:
    print("Only one weekend day had more than 100 deliveries.")
else:
    print("Neither weekend day had more than 100 deliveries.")