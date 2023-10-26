class CPerson:
    def __init__(self, name, lastName, surname, day, month, year, gender):
        self.name = name
        self.lastName = lastName
        self.surname = surname
        self.day = day
        self.month = month
        self.year = year
        self.gender = gender

    def __del__(self):
        print('Очищенно')

person1 = CPerson(input('name: '), input('Lastname: '),input('surname: '), input('day: '), input('month: '), input('year: '), input('gender: '))
print(f'ФИО - {person1.name} {person1.lastName} {person1.surname}, \nДата рождения - {person1.day}.{person1.month}.{person1.year},\ngender - {person1.gender}')
