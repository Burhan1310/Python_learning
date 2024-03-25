coordinates = []
x = int(input('x: '))
y = int(input('y: '))
z = int(input('z: '))
n = int(input('n: '))


# for i in range(x+1):
#     for j in range(y+1):
#         for k in range(z+1):
#             if i+j+k != n:
#                 coordinates.append([i, j, k])
#
# print(coordinates)

# newlist = [[i for i in range(x + 1)],
#            [j for j in range(y + 1)],
#            [k for k in range(z + 1)] if (i+j+k) != n]
#     print(newlist)


# hello =[i+j+k !=n for i,j,k in range(x+1, y+1, z+1)]
# print(hello)

newlist = [[i] + [j] + [k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]
print(newlist)