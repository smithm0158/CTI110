name = input('Whats the employee\'s name?')
hours_worked = float(input('How many hours worked?'))
pay_rate = float(input('What is the pay rate?'))


if (hours_worked > 40):
    reg_pay = 40 * pay_rate
    ot_hours = hours_worked - 40
    ot_pay = ot_hours * (pay_rate * 1.5)
    total_pay = ot_pay + reg_pay

else:
    ot_pay = 0
    ot_hours = 0
    reg_pay = hours_worked * pay_rate
    total_pay = ot_pay + reg_pay

print('----------------------------------------------------') 
print('Employee\'s Name:   ', name)
print()
print('Hours Worked\tPay Rate\tOverTime\tOverTime Pay\tRegHour Pay\tGross Pay')
print('-'*81)
print(hours_worked,'\t\t', end ='')
print(pay_rate, '\t\t',end ='')
print(ot_hours, '\t',end = '')
print('\t${:,.2f}'.format(ot_pay), end ='')
print('\t\t${:,.2f}'.format(reg_pay), end ='')
print('\t\t${:,.2f}'.format(total_pay), end ='')



#Variables
#Declare String name
#Declare Real hours_worked, pay_rate, reg_pay, ot_hours, ot_pay, total_pay


#Input
#   Display "Whats the name of the employee?"
#   Get name
#
#   Display "How many hours worked?
#   Get hours_worked
#
#   Display "What is the rate of pay?
#   Get pay_rate

#Calculations
#if (ot_hours >40) then
   # reg_pay = 40 * pay_rate
    #ot_hours = hours_worked - 40
    #ot_pay = ot_hours * (pay_rate * 1.5)
    #total_pay = ot_pay + reg_pay
   #else
   #ot_pay = 0
    #ot_hours = 0
    #reg_pay = hours_worked * pay_rate
    #total_pay = ot_pay + reg_pay
#Output
   #Display"Employee name is:", employee name
   #Display hours worked
  # Display ot_hours
   #Display ot_pay
   # Display reg_pay
   # Display Gross_pay
