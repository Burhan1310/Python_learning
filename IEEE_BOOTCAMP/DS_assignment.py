# Exercise 1: List Manipulation
# 1. Initializes an empty list.
my_list = []
print(type(my_list))
# 2. Appends the numbers 1 to 5 to the list.
for x in range(1, 6):
    my_list.append(x)

print(my_list)
# 4. Inserts the number 10 at index 2.
my_list.insert(2, 10)
print(my_list)
# 5. Removes the element at index 3.
my_list.remove(3)
# 6. Prints the modified list.
print('The modified list is : ', my_list)

# Exercise 2: Tuple Operations
# 1. Initializes two tuples with some elements (e.g., tuple_a = (1, 2, 3) and tuple_b = (3, 4, 5)).
tuple1 = (1, 2, 'IEEE', 'IU', 'Kushtia', 3.14)
tuple2 = (4, 5, 'Campus', 'Jubaer', 'Burhan', 8.98)
# 2. Prints the concatenation of the two tuples.
concatenate_tuple = tuple1 + tuple2
print(concatenate_tuple)
# 3. Prints the result of multiplying the second tuple by 3.
print(tuple2 * 3)

# Exercise 3: Set Operations
set_a = {'IU', 'IEEE', 1, 2, 4}
set_b = ['Kushtia', 'IU', 10, 20, 'BAN']
union_set = set_a.union(set_b)
print(union_set)
intersect_set = set_a.intersection(set_b)
print(intersect_set)
set_a.update(set_a.intersection(set_b))
print(set_a)
# Prints the elements present in set A, but not in set B.
print(set_a.difference(set_b))
# Prints the symmetric difference between the two sets.
print(set_a.symmetric_difference(set_b))

# Exercise 4: List Comprehension
# 1. Initializes a list with numbers from 1 to 10.
new_list = [i for i in range(1, 11)]
print(new_list)
#  2. Creates a new list containing the squares of each number in the first list.
square_list = [i ** 2 for i in new_list]
print(square_list)
# 3. Creates another list containing only the even numbers from the first list.
even_list = [i for i in new_list if i % 2 == 0]
print(even_list)



