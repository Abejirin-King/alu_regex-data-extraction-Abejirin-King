import re

text = """
Here are some emails: user@example.com, firstname.lastname@company.co.uk.
Some URLs: https://www.example.com, https://subdomain.example.org/page.
Phone numbers: (123) 456-7890, 123-456-7890, 123.456.7890.
Credit cards: 1234 5678 9012 3456, 1234-5678-9012-3456.
"""

email_regex = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
url_regex = r'https?://[a-zA-Z0-9.-]+(?:\.[a-zA-Z]{2,})(?:/[^\s]*)?'
phone_regex = r'(\(\d{3}\)\s?\d{3}[-.]\d{4}|\d{3}[-.]\d{3}[-.]\d{4})'
credit_card_regex = r'\b(?:\d{4}[- ]?){3}\d{4}\b'

emails = re.findall(email_regex, text)
urls = re.findall(url_regex, text)
phones = re.findall(phone_regex, text)
credit_cards = re.findall(credit_card_regex, text)

print("Emails:", emails)
print("URLs:", urls)
print("Phone Numbers:", phones)
print("Credit Cards:", credit_cards)
