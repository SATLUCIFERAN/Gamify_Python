
class Dog:
    def __init__(self, name):
        self.name = name        

    def bark(self):
        print(f"{self.name} says: Woof!")  


spot = Dog("Spot")  # create an instance
spot.bark()         # Spot says: Woof!
