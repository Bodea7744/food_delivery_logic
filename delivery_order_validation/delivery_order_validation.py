# Order Validation

# Entering the number of items in the delivery
while True:
    number_of_items = int(input("Enter the total number of items in the delivery: "))
    if 1 <= number_of_items <= 50:
        break
    print("Error: Invalid number of items.")

# Entering the delivery value
while True:
    delivery_price = float(input("Enter the delivery price: "))
    if delivery_price > 0:
        break
    print("Error: Price must be greater than 0.")

# Entering the payment status
while True:
    payment_status = input("Enter the payment status (paid/unpaid/pending): ")
    if payment_status == "paid":
        print(f"Number of items: {number_of_items}, price: {delivery_price}, payment status: {payment_status}")
        break
    elif payment_status == "unpaid" or payment_status == "pending":
        print("Delivery is not paid, it cannot be processed.")
    else:
        print("Error: Unknown payment status.")