numbers = [2,4,6,7, 5, 84,43,3]
numbers.append(56)
numbers.insert(1, 45)
numbers.remove(45)
numbers.pop()
print(numbers)
print(56 in numbers)
print(numbers.count(5))
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
numbers2 = numbers.copy()
numbers.append(65)
print(f'{numbers},  {numbers2}')



numbers3 = [3,4,4,53,2,2,4,546]
unique = []
for duplicates in numbers3:
    if duplicates not in unique:
        unique.append(duplicates)
print(f'The unique List is {unique}')
