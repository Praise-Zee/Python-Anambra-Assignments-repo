incomeAmount = int(input("Enter your Monthly income"))
incomeDescription = input("Enter income description")
expenseAmount = int(input("Enter expenses"))
expenseDescription = input("Enter expense description")
2expenseAmount = int(input("Enter 2nd expense"))
2expenseDescription = input("Enter 2nd expenxe description")
Totalexpense = expenseAmount + 2expenseAmount
netSaving = incomeAmount - Totalexpense
print("Your income is" + incomeAmount "while your expense is" + Totalexpense "therefore your balance is" + netSaving)
