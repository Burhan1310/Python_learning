class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"

    def myfunc(self):
        print("Hello this is " + self.name)


person1 = Person("Mowmita", 23)
print(person1.name)
print(person1.age)
print(person1)  # without __str()__ function this is not possible
person1.myfunc()

person1.age = 40
