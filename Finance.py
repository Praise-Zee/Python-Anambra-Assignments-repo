import math
income = int(input("Enter your monthly income: ₦ "))
incomeDescription = input("Enter income description")
expense1 = int(input("Enter expense amount: ₦"))
expenseDescription1 = input("Enter expense description")
expense2 = int(input("Enter 2nd expense amount: ₦"))
expenseDescription2 = input("Enter 2nd expense description")
Totalexpense = expense1 + expense2
netSavings = income - Totalexpense
print("income: ₦",income, "Totalexpense: ₦", Totalexpense, "netSavings: ₦", netSavings)
