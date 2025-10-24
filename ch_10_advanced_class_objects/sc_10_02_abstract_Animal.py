from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def speak(self):
        pass 

    @abstractmethod
    def movement(self):
        pass

class Dog(Animal):  # Subklasse av Animal
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):  # implementerer speak
        return "Woof!"
    
    def movement(self): # implementerer movement
        return "Run"

class Cat(Animal):  # Subklasse av Animal
    def speak(self):  # implementerer speak    
        return "Meow!"
    
    def movement(self):  # implementerer movement
        return "Sneak"

animals = [Dog("Fido", "Labrador"), Cat("Misty")]

for animal in animals:
   print(f"{animal.name} sier: {animal.speak()} bevegelse: {animal.movement()}")

another_animal = Animal("ImpossibleAnimal")
another_animal.speak()