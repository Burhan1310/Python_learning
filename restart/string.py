a = 'Hello World!'
print(a[1])  # strings are arrays

# looping through a String
for x in 'banana':
    print(x)

print('The length is ' + str(len(a)))

# check string
txt = 'The world cup is hosted by India'
print('mug' in txt)

if 'cup' in txt:
    print("yes,'cup' is present")

print('mug' not in txt)

if 'mug' not in txt:
    print("No, 'mug' is not present")

# slicing string
print(a[3:6])
print(a[:7])   # slice from the start
print(a[5:])   # slice to the end



# modifying string

print(a.upper())
print(a.lower())

a = '  hey there! '
print(a.strip())   # removing whitespace
print(a.replace('h', 'j'))
print(a.split())


# Concatenation
# concatenate = combine
a = 'Burhan'
b = 'Joy'
c = a + ' ' + b
print(c)


# format string
# combine string and numbers
age = 23
txt = 'My name is Burhan, and I am {}'
print(txt.format(age))

quantity = 5
itemNo = 546
price = 45.89
myOrder = 'I want {} pieces of item {} for {} dollars.'
print(myOrder.format(quantity, itemNo, price))

# escape
txt = 'We are the student of \'ICT\''
print(txt)
