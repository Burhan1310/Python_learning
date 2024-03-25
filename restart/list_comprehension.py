mylist = ['apple', 'banana', 'orange', 'cherry']
[print(x) for x in mylist]

# without list comprehension
newList = []

for x in mylist:
    if 'a' in x:
        newList.append(x)

print(newList)

# with list comprehension
newList = [x for x in mylist if 'a' in x]
print(newList)


newList = [x for x in mylist if x != 'apple']
print(newList)


newList = [x for x in range(10)]
print(newList)

newList = [x for x in range(10) if x < 5]
print(newList)

newList = [x.upper() for x in mylist]
print(newList)

newList = [x if x != 'banana' else 'orange' for x in mylist]
print(newList)