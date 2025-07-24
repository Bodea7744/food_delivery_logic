# Recipient Delivery Analysis

# User data input
while True:
    recipient_name = input("Enter the full recipient name: ")
    valid_name = recipient_name.split()

    if len(valid_name) < 2:
        print("Recipient name was not entered correctly, please re-enter the name: ")
    else:
        first_name = valid_name[0]
        last_name = " ".join(valid_name[1:])
        print(f"First Name: {first_name}, Last Name: {last_name}")
        break

# Input for number of past deliveries
while True:
    total_deliveries = int(input("Enter the number of deliveries made to this recipient in the past year: "))
    if total_deliveries <= 0:
        print("Number of deliveries was not entered correctly, please re-enter the number: ")
    else:
        break

# Input delivery amounts and calculate total spending
while True:
    total_spent = 0
    large_deliveries = 0

    for i in range(total_deliveries):
        amount = int(input(f"Enter the value of delivery {i+1}: "))
        total_spent += amount
        if amount > 10000:
            large_deliveries += 1

    print(f"Total amount spent on deliveries: {total_spent} lei")
    print(f"Number of high-value deliveries over 10,000 lei: {large_deliveries}")
    break

# Function to determine recipient status
def determine_status(total_spent, total_deliveries):
    if total_spent > 100000 and total_deliveries > 10:
        return "VIP", 10
    else:
        return "STANDARD", 5

status, discount = determine_status(total_spent, total_deliveries)

print(f"Recipient status for {first_name} {last_name}: {status}.")
print(f"A discount of {discount}% applies to future deliveries.")

# Ask for next delivery value
initial_price = float(input("Enter the price of your next delivery: "))

final_price = initial_price - (initial_price * discount / 100)

print(f"The final price after applying the discount is: {final_price:.2f} lei")