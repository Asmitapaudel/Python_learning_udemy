print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))


total_bill=float((bill/people)*(1+(tip/100)))

# print(f"Each of you will pay: {total_bill:.2f}")
print(f"Each person pays {round(total_bill,2)}")