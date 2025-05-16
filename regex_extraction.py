import re

# Regex patterns
email_pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
phone_pattern = r'^(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})$'
url_pattern = r'^https?:\/\/[^\s/$.?#].[^\s]*$'

# Function to validate input with a regex
def get_valid_input(prompt, pattern):
    while True:
        user_input = input(prompt)
        if re.match(pattern, user_input):
            return user_input
        else:
            print("Wrong input. Please try again.\n")

# Main program
email = get_valid_input("Enter your email address: ", email_pattern)
phone = get_valid_input("Enter your phone number: ", phone_pattern)
url = get_valid_input("Enter a website URL (starting with http or https): ", url_pattern)

print("\nThank you! All inputs are valid.")

