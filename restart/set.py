thisset = {'apple', 'banana', 'cherry'}
print(thisset)

# duplicate not allowed
set1 = {'melon', 'guava', 'cherry', 'mango'}
print(set1)

if 'banana' in thisset:
    print('yes')

thisset.add('orange')
print(thisset)

thisset.update(set1)
print(thisset)

thisset.remove('cherry')
thisset.discard('guava')
print(thisset)

# remove a random item
thisset.pop()
print(thisset)

# loop
for x in thisset:
    print(x)


thisset = set1.union(thisset)
print(thisset)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)
print(x)