for x in range(4) :
    for y in range(3):
        print(f'({x}, {y})')

numbers = [2, 2, 2, 2, 7]

for number in numbers:
    output = ''
    for count in range(number):
        output +=  'X'
    print(output)