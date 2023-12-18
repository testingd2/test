class Тварина:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        pass

class Pet:
    def __init__(self, name):
        self.name = name

    def play(self):
        pass

class Dog(Тварина, Pet):
    def __init__(self, name, breed):
        Тварина.__init__(self, species="Собака")
        Pet.__init__(self, name=name)
        self.breed = breed

    def make_sound(self):
        return "Гаф!"

    def play(self):
        return f"{self.name} він грається."

my_dog = Dog(name="Непридумав", breed="лабрадор")

print(f"Імя моєї собаки {my_dog.name}.")
print(f"Це порода {my_dog.species} {my_dog.breed}.")
print(f"{my_dog.make_sound()}")
print(f"{my_dog.play()}")