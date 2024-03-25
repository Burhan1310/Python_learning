mylist = ['apple', 'banana', 'cherry']
print(mylist)
print(len(mylist))
list1 = ['abc', 64, True, 49, 'male']
print(list1)
print(type(mylist))
list2 = [2, 4, 23, 3, 45, 56, 32, 60, 35, 5]
print(list2)
max = list2[0]
for number in list2:
    if number > max:
        max = number
print(max)

# accessing list
print(list2[2])
print(list2[2:5])

if 'apple' in mylist:
    print("yes, 'apple' is in the list")


# change list item
mylist = ['apple', 'banana', 'cherry']
mylist[1] = 'orange'
print(mylist)
mylist[1:2] = ['watermelon', 'guava']
print(mylist)

mylist[1:3] = ['Grapes']
print(mylist)

# insert item
mylist.append('jack-fruit')
print(mylist)
mylist.insert(2, 'pineapple')
print(mylist)

# extend list
list3 = ['potato', 'tomato', 'chilli']
mylist.extend(list3)
print(mylist)

# add any iterable
tuple1 = ('kiwi', 'honey', 'lichi')
list3.extend(tuple1)
print(list3)

# remove item from list
list3.remove('honey')
print(list3)

# pop method removes the specified index
list3.pop(2)
print(list3)

# del keyword also removes the specified index
del list3[2]
print(list3)

# clear method empties the list
# list3.clear()
# print(list3)

list3.insert(3, 'honey')


# Loop through a list
for x in list3:
    print(x)


for i in range(len(list3)):
    print(list3[i])

# using while loop
i = 0
while i < len(list3):
    print(list3[i])
    i += 1


# sort list
list3.sort()     # by default alphanumerically
print(list3)


list4 = [3, 48, 57, 24, 23, 45, 545, 5, 45]
list4.sort(reverse=True)
print(list4)


# customize sort
def myfunc(n):
    return abs(n - 45)


list4.sort(key=myfunc)
print(list4)

# reverse sort
list4.reverse()
print(list4)

# copy a list
list5 = list3.copy()
print(list5)

# join lists
list6 = list3 + list4
print(list6)

for x in list4:
    list3.append(x)


print(list3)

list4.extend(list3)
print(list4)