
#print(phrase)
phrase = input('Please enter a phrase. You can enter d, done, or Done to quit. \n')
while (phrase != 'd') :
    print('{}'.format(phrase)[::-1])
    phrase = input()
    if phrase == 'done':
        break
    if phrase == 'Done':
        break
    if phrase == 'd':
        break
