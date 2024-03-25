x = 10
print(type(x))


class Car:
    def __init__(self, color, model):
        self.Color = color
        self.Model = model

    def display_info(self):
        print(f"The color of the car is {self.Color} & the model is {self.Model}")
        print(self)


car1 = Car(model="BMW", color='Black')
car2 = Car('white', 'Mercedes')
car1.display_info()
car2.display_info()
print(hex(id(car1)))
print(hex(id(car2)))
