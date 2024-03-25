# formatted string
name = 'Ayana'
age = 16
print(f'Name: {name}, Age: {age}')


# type casting

print(type(int('15')))
print(type('15'))

flower = ['rose', 'belly']
a = 'rose' in flower
print(a)
b = 'jasmine' in flower
print(b)

if 'jasmine' in flower:
    print('yes')
else:
    print('The flower is not available')


x = [1, 2, 3]
y = [1, 2, 3]
z = y
print(id(x))


