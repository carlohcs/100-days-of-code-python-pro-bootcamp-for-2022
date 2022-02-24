pcts = ("10", "12", "15") # Tuple
pcts_types = " or ".join(pcts)

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input(f"What percentage tip would you like to give? {pcts_types}? "))
people = int(input(f"How many people to split the bill? "))
amount = round(((bill * tip) / 100 + bill) / people, 2)
amount = "{:.2f}".format(amount)
print(f"Each person should pay: ${amount}")

