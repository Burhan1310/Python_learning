# f(x) = y
import lamda as lamda

def f(x):
    y = 2 * x ** 2 + 1
    return y


print(f(1))


def fn_name(name):
    t = f'IEEE IU SB {name}'
    return t.split()


y = fn_name('IU')
print(y)

# recursive function
def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)


print(factorial(4))
print(factorial(5))

# lamda function
f = lamda b: 2*b**2 + 1


