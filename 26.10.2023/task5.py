class Phone:
    def __init__(self, number, model, weight):
        self.number = number
        self.model = model
        self.weight = weight

    def receivePhone(self):
        self.name = 'Evgeny'
        print(f'Звонит {self.name}')

    def getNumber(self):
        print(self.number)
phone1 = Phone('123124124', 'Iphone', 0.17)
phone2 = Phone('123124413', 'Redmi', 0.22)
phone3 = Phone('123542554', 'Sumsung', 0.2)

phone1.receivePhone()
phone1.getNumber()
phone2.receivePhone()
phone2.getNumber()
phone3.receivePhone()
phone3.getNumber()