word = input('Input your password here: ')
password = ''
password = word.replace('i', '1')
password = password.replace('a', '@')
password = password.replace('m', 'M')
password = password.replace('B', '8')
password = password.replace('s', '$')
password = password + '!'
print('Your new password is: ', password)
