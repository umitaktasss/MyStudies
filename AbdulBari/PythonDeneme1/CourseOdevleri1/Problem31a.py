import random
class Animal():
    def __init__(self, Name: str, Species: str, Age: int):
        self.Name = Name
        self.Species = Species
        self.Age = Age

    def __str__(self) -> str:
        return (f"************\n"
                f"Name: {self.Name}\n"
                f"Species: {self.Species}\n"
                f"Age: {self.Age}\n"
                f"************\n")

class Dog(Animal):
    def __init__(self, Name: str, Species: str, Age: int, Breed: str, Owner: str):
        super().__init__(Name, Species, Age)
        self.Breed = Breed
        self.Owner = Owner

    def Display_attributes_Dog(self) -> str:
        attributes = f"Name: {self.Name}\nSpecies: {self.Species}\nAge: {self.Age}\nBreed: {self.Breed}\nOwner: {self.Owner}"
        return attributes

    def bark(self) -> str:
        return f"{self.Name} is Barking!"

    def Change_Owner(self) -> None:
        change = input("New Owner:")
        self.Owner = change

class Bird(Animal):
    def __init__(self, Name: str, Species: str, Age: int, Wing_span: str, Nest_Type: str):
        super().__init__(Name, Species, Age)
        self.Wing_Span = Wing_span
        self.Nest_Type = Nest_Type

    def Display_attributes_Bird(self) -> str:
        attributes = f"Name: {self.Name}\nSpecies: {self.Species}\nAge: {self.Age}\nWing Span: {self.Wing_Span}\nNest Type: {self.Nest_Type}"
        return attributes

    def fly(self) -> str:
        return f"{self.Name} is Flying Now!"

    def chirp(self) -> str:
        a = random.randint(0, 1)
        if a == 0:
            return f"{self.Name} is not in a good mood to chirp"
        else:
            return f"{self.Name} is chirping amusingly!"

class Horse(Animal):
    def __init__(self, Name: str, Species: str, Age: int, Breed: str, Color: str):
        super().__init__(Name, Species, Age)
        self.Breed = Breed
        self.Color = Color

    def Display_attributes_Horse(self) -> str:
        attributes = f"Name: {self.Name}\nSpecies: {self.Species}\nAge: {self.Age}\nBreed: {self.Breed}\nColor: {self.Color}"
        return attributes

    def gallop(self) -> str:
        return f"{self.Name} is Galloping!"

    def rear_up(self) -> str:
        return f"{self.Name} is Rearing Up!"