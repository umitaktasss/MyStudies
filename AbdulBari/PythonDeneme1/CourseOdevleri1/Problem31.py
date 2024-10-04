
from Problem31a import *
 # Animal objects
animal_1 = Animal("Max", "Dog", 5)
animal_2 = Animal("Tweety", "Bird", 2)
animal_3 = Animal("Thunder", "Horse", 7)

# Dog object
dog_1 = Dog("Buddy", "Dog", 3, "Labrador", "John")
print(dog_1)
print(dog_1.Display_attributes_Dog())
print(dog_1.bark())
dog_1.Change_Owner()
print(dog_1.Display_attributes_Dog())

# Bird object
bird_1 = Bird("Kiwi", "Bird", 1, "20 cm", "Cavity")
print(bird_1)
print(bird_1.Display_attributes_Bird())
print(bird_1.fly())
print(bird_1.chirp())

# Horse object
horse_1 = Horse("Spirit", "Horse", 6, "Mustang", "Black")
print(horse_1)
print(horse_1.Display_attributes_Horse())
print(horse_1.gallop())
print(horse_1.rear_up())
