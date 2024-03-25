thisdict = {
    'brand': 'ford',
    'model': 'Mustang',
    'year': 1956
}
print(thisdict)
print(thisdict['brand'])
print(type(thisdict))

# for x in thisdict:
#     print(x)
#
# print(thisdict.keys())

x = thisdict.keys()
print(x)

thisdict['color'] = 'white'
print(x)
print(thisdict)

thisdict['color'] = 'black'
print(thisdict)

print(thisdict.items())

print(thisdict.values())


if 'model' in thisdict:
    print('yes')


# change the value

thisdict['year'] = 2020
print(thisdict)

thisdict.update({'year': 2019})
print(thisdict)

# adding item

thisdict['type'] = 'sports'
print(thisdict)

# removing items
thisdict.pop('color')
print(thisdict)
thisdict.popitem()
print(thisdict)

del thisdict['year']
print(thisdict)

for x in thisdict:
    print(thisdict[x])


for x in thisdict.values():
    print(x)


mydict = thisdict.copy()
print(mydict)

# nested dictionaries
myFamily = {
    'child1': {
        'name': 'Emilly',
        'age': 14
    },
    'child2': {
        'name': 'Jessy',
        'age': 9
    },
    'child3': {
        'name': 'Emilly',
        'age': 14
    }
}
print(myFamily)