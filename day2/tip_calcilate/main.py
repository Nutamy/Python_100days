print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill?\n"))
people = float(input("How many people to split the bill?\n"))
percentage = float(input("What percentage tip woul you like to give?\n"))/100+1
result = total_bill*percentage/people
print(f"Each person should pay: {result:.2f}")