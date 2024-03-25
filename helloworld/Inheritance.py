class Mammal:
    def walk(self):
        print("Walk")


class Dog(Mammal):
    def bark(self):
        print("Barking The Dog")


class Cat(Mammal):
    pass


dog1 = Dog()
dog1.bark()

cat = Cat()
cat.walk()
cat.x = 10
print(cat.x)

