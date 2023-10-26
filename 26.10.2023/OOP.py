class Person:
    kind = 'Человек'

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f'Родился - {self.name}')

    def __del__(self):
        print('Уничтожен', self.name)

    def say_hello(self):
        print('hello!')

    def send_message(self, message='bye'):
        print(message)

    def say(self):
        self.say_hello()


tom = Person('Tom', 18)
tom.say_hello()
tom.say()
tom.send_message('message')
tom.height = 1.75
print(tom.height)

bob = Person('Bob', 34)
