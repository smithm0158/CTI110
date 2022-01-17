#A program that claculates miles per gallon, and the cost per gallon
#10/40/21
#CTI-110 P2HW1-Miles Per Gallon
#Michael Smith
#

driven = int(input("Enter miles driven: "))
gallons = int(input("Enter gallons used: "))
cost= float(input('Enter cost per gallon: '))

gallons_used = (driven / gallons)
gas_cost = (cost * gallons)
cpm = (cost / driven)

print()
print('Miles Per gallon: ','{:.2f}'.format(gallons_used))
print('Total Gas Cost:   ', '${:.2f}'.format(gas_cost))
print('Cost Per Mile:    ', '${:.2f}'.format(cpm))




#Variables
#Declare Real driven, gallons, cost

#Input
#Display ('How many miles driven?')
#Input driven
#Display ('How many gallons used?')
#Input gallons
#Display ('Enter cost per gallon')
#Input Cost

#calculations
#gallons_used = (driven / gallons)
#gas_cost = (cost * gallons)
#cpm = (cost / driven)

#display
#Display "Miles per gallon: gallons_used"
#Display "Total gas cost: gas_cost"
#Display "Cost Per Mile: cpm"
