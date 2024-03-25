thisTuple = ('apple', 'banana', 'cherry')
print(thisTuple)
print(len(thisTuple))

# creating tuple with single item
myTuple = ('orange',)
print(myTuple)

# NOT a tuple
myTuple = 'orange'
print(myTuple)


# data_type
print(type(myTuple))

# access tuples items
print(thisTuple[1])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:6])
print(thistuple[:5])
print(thistuple[3:])

if 'apple' in thistuple:
    print("yes, 'APPLE' is in thistuple")


# Change tuple values
x = ('apple', 'banana', 'cherry')
print(x)
y = list(x)
y[1] = 'kiwi'
x = tuple(y)
print(x)

# add item
y = list(x)
y.append('orange')
x = tuple(y)
print(x)

for x in thistuple:
    print(x)

for i in range(len(thistuple)):
    print(thistuple[i])


i = 0
while i < len(thistuple):
    print(thistuple[i])
    i += 1
