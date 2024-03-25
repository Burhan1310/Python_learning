class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def draw(self):
        print("Draw")
    def move(self):
        print("Move")


point = Point(10, 20, 30)
point.z = 45
print(point.z)


