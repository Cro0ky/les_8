class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def info(self):
        print(f'x = {self.x}, y = {self.y}, z = {self.z}')

    def distance(self):
        dxy = self.y - self.x
        szy = self.z - self.y
        print(f'Расстояние между ху: {dxy}, Расстояние между ху: {szy}')


a = Point3D(1, 2, 3)
b = Point3D(4, 5, 6)
c = Point3D(7, 8, 9)
a.info()
b.info()
c.info()
a.z = 123132
a.info()
a.distance()