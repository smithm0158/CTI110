caffeine_mg = float(input('Enter how much caffeine in the drink: '))

''' Type your code here. '''
halfLife = caffeine_mg / 2
halfLife2 = ((halfLife)/2)
halfLife3 = ((halfLife2)/4)

print('After 6 hours:','{:.2f}'.format(halfLife), 'mg')
print('After 12 hours:','{:.2f}'.format(halfLife2), 'mg')
print('After 24 hours:','{:.2f}'.format(halfLife3), 'mg')
