x = 5
y = 'HELLO World'
x = 'burhan'
print(x)
print(y)

print(type(x))
print(type(y))

# multiple variables
a, b, c, d = 'Jubaer', 'Atik', 'Foysal', 45
print(a)
print(b)
print(c)
print(d)

#Output Multiple variable
print(a, b, c, d)
print(a + b + c)

s = 342324
t = 34734
print(s+t)

#global and local variables
def myfunc():
    a = 'Sajid'   #local variable
    print('His name is ' + a)
    global p
    p = 'python'
myfunc()
