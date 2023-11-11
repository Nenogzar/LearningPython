import re

email = "den@sales.example.com"

pattern = r"^([a-z0-9_.-]+)@(([a-z0-9-]+\.)+[a-z]{2,6})$"
p = re.compile(pattern, re.I | re.S)

m = p.search(email)

if not m:
	print("Not match")
else:
	print("Match")
