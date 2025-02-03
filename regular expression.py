import re

gmail = input("Enter your gmail: ").strip()

if re.search(r"^[x\w\.]+@(\w.\.)?\w+\.(com|edu)$", gmail, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")