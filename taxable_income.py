income = float(input("Enter your taxable income:"))

if income <= 20000:
    tax = 0.02 * income
elif income <= 50000:
    tax = 400 + .025 * (income - 20000)
else:
    tax = 1150 + 0.035 * (income - 50000)

print("The state income tax is", tax)
