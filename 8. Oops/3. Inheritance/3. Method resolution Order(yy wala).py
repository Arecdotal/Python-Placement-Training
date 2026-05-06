from abc import ABC,abstractmethod
class Animal(ABC):
    def sound(self):
        print("Gutur Gu...Gutur Gu From Animal")
    
class Bird(ABC):
    def sound(self):
        print("Koo...Koo... From Bird")
        
    @abstractmethod
    def fly():
        pass
    
class Pigeon(Animal, Bird):
    def fly(self):
        print("Flying...")
        
p = Pigeon()
p.sound()
p.fly()