# Recipient Name Validation

# Define the function for counting vowels
def count_vowels(name):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    counter = 0
    for letter in name:
        if letter in vowels:
            counter += 1
    return counter

# Start the loop for entering recipient names
while True:
    recipient_name = input("Enter the recipient's name: ")
    vowel_count = count_vowels(recipient_name)

    # Display the number of vowels and continue execution until stop condition
    print(f"The name '{recipient_name}' contains {vowel_count} vowels.")

    if vowel_count == 0:
        print("The name contains no vowels. The program will now exit.")
        break