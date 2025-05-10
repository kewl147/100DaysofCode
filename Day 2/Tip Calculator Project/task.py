print("Welcome to the tip calculator!\n")
bill = float(input("What was the total bill? \n$"))
tip = int(input("What percentage tip would you like to give? \n10 12 15 \n"))
people = int(input("How many people to split the bill? \n"))

tipTotal = bill * tip / 100
totalBill = bill + tipTotal
totalPerPerson = round(float((bill + tipTotal)/people), 2)
mismatch = round((totalPerPerson * people) - totalBill, 2)

print(f"Your total bill with tip is ${totalBill:.2f}")
print(f"Each person should pay ${totalPerPerson:.2f}")
print(f"There will be a mismatch of ${mismatch:.2f}")
