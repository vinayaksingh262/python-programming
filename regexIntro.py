import re


mo = re.search(r"\d{3}-\d{3}-\d{4}", "My number is 415-555-4242.")

if mo:
    print(f"Phone number found: {mo.group()}")
else:
    print("No phone number found.")
