class Animal:  # Foreldreklasse, arver fra object
    def __init__(self, name):
        self._name = name

    def speak(self):
        return "Some generic animal sound"

class Dog(Animal):  # Subklasse av Animal
    def __init__(self, name, breed):
        super().__init__(name)  # Kall til foreldreklassens __init__
        self.breed = breed

    def speak(self):  # Overstyrer speak fra Animal
        return "Woof!"

class Cat(Animal):  # Subklasse av Animal
    def speak(self):  # Overstyrer speak fra Animal
        return "Meow!"

# Polymorfi i praksis:
animals = [Dog("Fido", "Labrador"), Cat("Misty"), Animal("Generic")]

for animal in animals:
   print(f"{animal._name} sier: {animal.speak()}")