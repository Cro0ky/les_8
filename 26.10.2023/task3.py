class Triangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def ploshad(self):
        print(f'Площадь треугольника = {0.5 * (self.a * self.b)}')

    def perimetr(self):
        self.c = (self.a ** 2 + self.b ** 2) ** 0.5
        print(f'Периметр треугольника = {self.a + self.b + self.c}')


tr1 = Triangle(3, 5)
tr1.ploshad()
tr1.perimetr()
