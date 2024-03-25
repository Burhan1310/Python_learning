# list
my_list = [1, 2, 'hello', 3.14, 'IEEE', 'IU', 45]
print(my_list[0])
print(my_list[-1])
print(my_list[1:3])

print(type(my_list))

# add single item
my_list.append(2023)
print(my_list)

# for multiple item
my_list.extend([4, 5, 7])
print(my_list)

# add item at different index
my_list.insert(5, "Burhan")
print(my_list)

# searching
print(my_list.index('Burhan'))

# remove items
print(my_list.remove(4))
print(my_list)

print(my_list.reverse())
print(my_list)

square = []
for i in range(5):
    square.append(i ** 2)

print(square)

# list comprehension
new_list = [i ** 2 for i in range(5) if i > 1]
print(new_list)

# set
# creating set
my_set = {1, 2, 5.4, 'IEEE', 'IU', 'Kushtia', 'IU'}
print(my_set)
print(type(my_set))

# creating set using function
fruits = set(['banana', 'apple', '1', 2])
print(type(fruits))

# set method
my_set.add('Burhan')
print(my_set)
my_set.remove('Burhan')
print(my_set)
# using discard
my_set.discard('IU')
print(my_set)
my_set.discard('Joy')
print(my_set)
new_set = {1, 2, 3, 45, 'Jubayer', 'IEEE', 'IU'}
popped_item = new_set.pop()
print(popped_item)
# my_set.clear()
Set = set()
print(type(Set))

# mathematics operation of set
# union operation
set_a = {'IU', 'IEEE', 1, 2, 4}
set_b = ['Kushtia', 'IU', 10, 20, 'BAN']

union_set = set_a.union(set_b)
print(union_set)

# intersection operation
intersection_set = set_a.intersection(set_b)
print(intersection_set)

# difference between two sets
difference_set = set_a.difference(set_b)
print(difference_set)

# symmetric difference
set_1 = {1, 2, 3}
set_2 = {3, 4, 5}
symmetric_set = set_1.symmetric_difference(set_2)
print(symmetric_set)

# Subset operation
set_A = {1, 2, 3}
set_B = {1, 2, 3, 5}
is_subset = set_A.issubset(set_B)
print(is_subset)

# update operation
set_x = {12, 23, 34, 45}
set_y = {21, 12, 23, 78}
set_x.update(set_y)
print(set_y)
print(set_x)

# adding multiple set into one set


# dictionary
# creating dictionary
# method1
Dict = {
    'name': 'Burhan',
    'Age': 23,
    'Home': 'Habiganj'
}
print(type(Dict))
print(Dict)
# creating dictionary using function
dict2 = dict(name='Alice', Age=23, city='Dhaka')
print(dict2)
print(dict2['name'])
print(dict2.keys())
print(dict2.values())
print(dict2.items())

# updating values
dict2['name'] = 'Jubaer'
print(dict2)
# removing key valu pair
dict2.pop('Age')
print(dict2)
dict2.popitem()
print(dict2)

test_dict = dict([('Varsity', 'IU'), ('City', 'Kushtia'), ('Dept', 'ICT')])
print(test_dict)

# dictionary comprehension
square = {}
for num in range(5, 10):
    square[num] = num ** 2;


print(square)
com_square = {digit: digit ** 2 for digit in range(5, 11)}
print(com_square)

# live task
nameList = ['Burhan', 'Jubaer', 'Ayana', 'Hemayet', 'Shimanto']
name_len = {}
for length in nameList:
    name_len[length] = len(length)


print(name_len)
comp_Dict = {leng: len(leng) for leng in nameList}
print(comp_Dict)
