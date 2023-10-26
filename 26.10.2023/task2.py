class Squer:
    def __init__(self, a):
        self.a = a

    def ploshad(self):
        print(f'Площадь = {self.a * 2}')

    def perimetr(self):
        print(f'Периметр = {self.a * 4}')


kv1 = Squer(4)
kv1.ploshad()
kv1.perimetr()
