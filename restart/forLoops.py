fruits = ['apple', 'banana', 'cherry', 'orange']
for x in fruits:
    print(x)


# looping through a String
for x in 'banana':
    print(x)


# the break statement
for x in fruits:
    print(x)
    if x == 'cherry':
        break


for x in fruits:
    if x == 'cherry':
        break
    print(x)


# the continue statement
for x in fruits:
    if x == 'cherry':
        continue
    print(x)


# the range function
for x in range(6):
    print(x)