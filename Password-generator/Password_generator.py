import random

print('Welcome to the password generator')
print('*********************************')

chars = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789!@#$%^&*?'
number = input('Amount of passwords: ')
number = int(number)

lenght = input('Enter lenght of password: ')
lenght = int(lenght)

print('\nhere is your Password')
for pwd in range(number):
    password = ''
    for c in range(lenght):
        password += random.choice(chars)
        print(password)
