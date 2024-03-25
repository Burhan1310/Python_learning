a = 48
b = 567
if b > a:
    print('b is greater than a')


b = 48
if b > a:
    print('b is greater than a')
elif a == b:
    print('a and b are equal')


b = 22
if b > a:
    print('b is greater than a')
elif a == b:
    print('a and b are equal')
else:
    print('a is greater than b')


a = 56
b = 5675
print('A') if a > b else print('B')
a = 56
b = 56
print('A') if a > b else print('=') if a == b else print('B')

a = 200
b = 33
c = 500
if b < a < c:
    print('both condition are TRUE')


if a > b or a > c:
    print('at least one of the conditions is TRUE')


if not a < b:
    print('b is not greater than a')


x = 41
if x > 10:
    print('Above ten,')
    if x > 20:
        print('and also above 20!')
    else:
        print('not above 20.')