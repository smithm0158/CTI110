#Learning to use math in IDLE
#9/22/21
#CTI-110 P1HW2 - Basic Math
#Michael Smith
#


expense_name =input("Enter name of expense: ")

expense = float(input('Enter monthly charge: '))
TAX = .06
#print(expense_name)
#print(expense)

tax_total = (expense * TAX)
total = (expense + tax_total)
annual = (total * 12)

print('Bill: ',expense_name, ' ----------- Before Tax: $', '{:.2f}'.format(expense))

print('Monthly tax: $', '{:.2f}'.format(tax_total))
print('Monthly total: $','{:.2f}'.format(total))
print('Annual Charge: $', '{:.2f}'.format(annual))

#
#declare variables
#Declare float expense, annual, total, tax_total
#Declare String expense_name
#Set Constant TAX = .06

#Get Input
#Display 'What is the name of the expense?'
#Get input expense_name
#Display 'How big is the expense?'
#Get input expense


#Calculations
#tax_total = (expense * TAX)
#total = (expense + tax_total)
#annual = (total * 12)

#Output
#Display ('Bill: $',expense_name)
#Display ('Before tax:', expense)
#Display ('Monthly Tax:', tax_total)
#Display ('monthly total:', total)
#Display ('Annual charge', annual)
