numbers = [3, 5, 34, 56, 4, 5, 43, 44]
print(numbers)
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)