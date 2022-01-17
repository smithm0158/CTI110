# CTI-110
# P2HW2 - List and Sets
# Michael Smith
# 10/4/21
#

num1 = int(input('Enter num 1: '))
num2 = int(input('Enter num 2: '))
num3 = int(input('Enter num 3: '))
num4 = int(input('Enter num 4: '))
num5 = int(input('Enter num 5: '))
num6 = int(input('Enter num 6: '))

nums = [ num1, num2, num3, num4, num5, num6]
avg= float(sum(nums)/6)
num_set = set(nums)

print()
print('Created List: ', nums)
print('smallest number in list: ', min(nums))
print('biggest number in list: ', max(nums))
print('sum of list: ', sum(nums))
print('avg of list: ', '{:.2f}'.format(avg))

print()
print (num_set)


#variables
#Declare Integer num1, num2, num3, num4, num5, num6
#Declare Real avg

#input
#Disply 'Enter number 1:'
#Input num1
#Disply 'Enter number 2:'
#Input num2
#Disply 'Enter number 3:'
#Input num3
#Disply 'Enter number 4:'
#Input num4
#Disply 'Enter number 5:'
#Input num5
#Disply 'Enter number 6:'
#Input num6

#calculations
#nums = [num1, num2, num3, num4, num5, num6]
#avg = float(sum(nums)/6)
#num_set = set(nums)

#output
#Display 'Created List'
#Display nums

#Display 'smallest number in list: '
#Display min(nums)

#Display 'biggest number in list: '
#Display max(nums)

#Display 'sum of list: '
#Display sum(nums)

#Display 'Avg of list: '
#Display avg

