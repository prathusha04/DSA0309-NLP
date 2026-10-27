import re
text = "Python is easy. Contact us at student123@gmail.com"
# Search for a word
match = re.search(r"easy", text)
if match:
    print("Word found:", match.group())
# Find all email addresses
emails = re.findall(r"[\w.-]+@[\w.-]+\.\w+", text)
print("Email addresses:", emails)
# Match a string starting with Python
if re.match(r"Python", text):
    print("The text starts with Python")
# Replace a word
new_text = re.sub(r"easy", "powerful", text)
print("Modified text:", new_text)
