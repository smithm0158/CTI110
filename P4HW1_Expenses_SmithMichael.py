#CTI-110
#P4HW1 - Expenses
#Michael SMith
#11/1/21

account_bal = float(input("Enter starting balance of account: "))
print()

expense1 = float(input("Enter expense 1: "))
end_bal= account_bal - expense1
counter = 1

#print()
#print("account balance is: ", account_bal)
#print("end balance is: ", end_bal)
suspend = input("Do you want to enter another expense? (y/n)")
print()

while suspend == 'y':
    expense2 = float(input("Enter expense: "))
    end_bal = end_bal - expense2
    #print("Resulting balance: ",end_bal)
    suspend = input("Do you want to enter another expense? (y/n) ")
    print()
    counter = counter + 1
    
print("Amount in account before expenses: ", '${:,.2f}'.format(account_bal))
print("Expenses entered: ", counter)
print("Ending balance is : ", '${:,.2f}'.format(end_bal))
