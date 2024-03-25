# make a simple calculator
def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiplication(num1, num2):
    return num1 * num2


def division(num1, num2):
    return num1 / num2


print('''Please Select an operation you want -\n
         1. Add
         2. Subtract
         3. Multiply
         4. Division''')

select = int(input('Pleaese select operation from 1, 2, 3, 4 : '))
number1 = int(input('Enter your first number: '))
number2 = int(input('Enter your second number: '))

if select == 1:
    print(f'\nThe Addition of {number1} and {number2} is : ', add(number1, number2))


elif select == 2:
    print(f'\nThe Subtraction from {number1} to {number2} is : ', subtract(number1, number2))


elif select == 3:
    print(f'\nThe Multiplication of {number1} and {number2} is : ', multiplication(number1, number2))


elif select == 4:
    print(f'\nThe Division of {number1} by {number2} is : ', division(number1, number2))

else:
    print('\nInvalid input, Please enter valid input')


# Assignment 2

def contact_info(name, email, phone):
    print(f'\nThe contact information is given : \n'
          f'My name is : {name} \n'
          f'My email is : {email} \n'
          f'My phone number is : {phone} \n')


contact_info('Burhan', 'burhanjoy2014@gmail.com', '01795952953')


# Assignment 3
def avg(*n):
    total = 0
    for num in n:
        total += num
    average = total / len(n)
    return average


print('The average of some arbitrary number is : ', avg(60, 50, 40))
