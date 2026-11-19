# Animal Sound Show (complete activity, DSCM2L5). Python 3 standard library only.
# Run: python animal_sound_show.py  (or paste into one Google Colab cell and press Run)
from abc import ABC, abstractmethod
import inspect


class Animal(ABC):                       # A: the parent class; (ABC) lets Python enforce abstract methods
    def __init__(self, name, habitat):
        self.name = name
        self.habitat = habitat

    def display(self):                   # B: every child inherits this method
        print(f"Name: {self.name} | Habitat: {self.habitat}")

    # Step 4: Make speak() abstract
    @abstractmethod
    def speak(self):                     # every child must write its own version
        pass


class Dog(Animal):                       # C: a worked example of a child class
    def __init__(self, name, habitat, breed):
        Animal.__init__(self, name, habitat)  # the direct way to run the parent constructor
        self.breed = breed

    def speak(self):
        print(f"{self.name} ({self.breed}) says: Woof! Woof!")


class Parrot(Animal):
    def __init__(self, name, habitat, phrase):
        # Step 2: Call the parent constructor
        super().__init__(name, habitat)
        if phrase == "":
            phrase = "Hello"
        self.phrase = phrase

    def speak(self):                     # E: the parrot repeats its phrase
        print(f"{self.name} says: {self.phrase}! {self.phrase}!")


class Lion(Animal):
    def __init__(self, name, habitat, pride):
        # Step 3: Lion's constructor
        super().__init__(name, habitat)
        self.pride = pride

    def speak(self):
        # Step 3: Lion's own speak()
        print(f"{self.name} (pride: {self.pride}) says: ROARRR!")


def run_show(animals):                   # F: one loop works for every child class
    if len(animals) == 0:
        print("No animals in the show yet.")
    for animal in animals:
        animal.display()
        animal.speak()


dog_name = input("Name of the dog? ")
show = [Dog(dog_name, "Home", "Labrador"), Parrot("Polly", "Jungle", "Pretty bird"),
        Parrot("Kiwi", "Jungle", ""), Lion("Simba", "Savannah", "Pride Rock")]
print("=== Animal Sound Show ===")
run_show(show)
run_show([])                             # G: edge case, an empty show
print("Is Animal abstract?", inspect.isabstract(Animal))
print("Bruno is an Animal:", isinstance(show[0], Animal), "| a Parrot:", isinstance(show[0], Parrot))
print("Lookup order for Lion:", [c.__name__ for c in Lion.__mro__])
