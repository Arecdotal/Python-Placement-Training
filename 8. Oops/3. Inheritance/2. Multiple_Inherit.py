# Multiple Inheritance

from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound():
        pass
    
class Bird(ABC):
    @abstractmethod
    def sound():
        pass
    @abstractmethod
    def fly():
        pass
    
class Pigeon(Animal, Bird):
    def sound(self):
        print("Gutur Gu...Gutur Gu")
    def fly(self):
        print("Flying...")
        
p = Pigeon()
p.sound()
p.fly()
