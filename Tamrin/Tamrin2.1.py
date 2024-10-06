class Vehicle:
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year

    def start(self):
        print('Vehicle srtarted')    


class Car(Vehicle):
    def __init__(self, name, model, year, doors):
        super().__init__(name, model, year)
        self.doors = doors

    def start(self):
        print('Car srtarted')


class Motoorcycle(Vehicle):
    def __init__(self, name, model, year, type):
        super().__init__(name, model, year)
        self.type = type

    def start(self):
        print('Motoorcycle srtarted')
        

C = Car('pezo', 'c4', '2020', 'type33')
B = Motoorcycle('para', 'A4', '2024', 'ty33')

C.start()
B.start()