# Base class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def move(self):
        raise NotImplementedError("Subclasses must implement move() method")
    
    def speak(self):
        return f"I am {self.name}"

# Different animal classes with polymorphic move() methods
class Dog(Animal):
    def move(self):
        return f"{self.name} is running! 🐕"
    
    def speak(self):
        return "Woof! Woof! 🐶"

class Bird(Animal):
    def move(self):
        return f"{self.name} is flying! 🕊️"
    
    def speak(self):
        return "Chirp! Chirp! 🐦"

class Fish(Animal):
    def move(self):
        return f"{self.name} is swimming! 🐟"
    
    def speak(self):
        return "Glub! Glub! 🐠"

class Snake(Animal):
    def move(self):
        return f"{self.name} is slithering! 🐍"
    
    def speak(self):
        return "Hiss! Hiss! 🐍"

# Vehicle polymorphism example
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def move(self):
        raise NotImplementedError("Subclasses must implement move() method")

class Car(Vehicle):
    def move(self):
        return f"{self.brand} {self.model} is driving on the road! 🚗"

class Airplane(Vehicle):
    def move(self):
        return f"{self.brand} {self.model} is flying in the sky! ✈️"

class Boat(Vehicle):
    def move(self):
        return f"{self.brand} {self.model} is sailing on water! ⛵"

class Bicycle(Vehicle):
    def move(self):
        return f"{self.brand} {self.model} is being pedaled on the path! 🚴"

# Demonstration function
def demonstrate_polymorphism():
    print("=== Animal Movement Demonstration ===")
    animals = [
        Dog("Buddy"),
        Bird("Tweety"),
        Fish("Nemo"),
        Snake("Slither")
    ]
    
    for animal in animals:
        print(animal.speak())
        print(animal.move())
        print()
    
    print("=== Vehicle Movement Demonstration ===")
    vehicles = [
        Car("Toyota", "Camry"),
        Airplane("Boeing", "747"),
        Boat("Yamaha", "242X"),
        Bicycle("Trek", "FX2")
    ]
    
    for vehicle in vehicles:
        print(vehicle.move())
        print()

# Create and test objects
if __name__ == "__main__":
    # Test Smartphone class
    print("=== Smartphone Demo ===")
    my_phone = Smartphone("Samsung", "Galaxy S23", 256)
    print(my_phone.unlock("0000"))
    print(my_phone.install_app("Game", 5))
    print(my_phone.get_status())
    print(my_phone.set_pin("1234"))
    print()
    
    # Test GamingPhone inheritance
    print("=== GamingPhone Demo ===")
    gaming_phone = GamingPhone("ASUS", "ROG Phone", 512, "Adreno 660", 16)
    print(gaming_phone.unlock("0000"))
    print(gaming_phone.enable_game_mode())
    print(gaming_phone.get_status())
    print()
    
    # Demonstrate polymorphism
    demonstrate_polymorphism()
