from abc import ABC, abstractmethod

class MarineAnimal(ABC):
    def __init__(self, name, habitat):
        self.name = name
        self.habitat = habitat

    @abstractmethod
    def move(self):
        print('MarineAnimal move !')

    @abstractmethod
    def eat(self):
        print('MarineAnimal eat !')    



class Fish(MarineAnimal):
    def __init__(self, name, habitat, fin_type, swim_speed):
        super().__init__(name, habitat)
        self.fin_type = fin_type
        self.swim_speed = swim_speed

    def move(self):
        print('Fish move')

    def eat(self):
        print('Fish eat')    



class Crustacean(MarineAnimal):
    def __init__(self, name, habitat, shell_type, crawl_speed):
        super().__init__(name, habitat)
        self.shell_type = shell_type
        self.crawl_speed = crawl_speed
        
    def move(self):
        print('Crustacean move')

    def eat(self):
        print('Crustacean eat')    


a = Fish('salmon', 'sea', 'blue', '50')
b = Crustacean('hipa', 'sea', 'red', '10')

a.move()
a.eat()

b.move()
b.eat()