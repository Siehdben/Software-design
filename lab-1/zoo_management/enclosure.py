from animal import Animal

class Enclosure:
    def __init__(self, name, enclosure_type, size):
        self.name = name
        self.enclosure_type = enclosure_type
        self.size = size
        self.animals = []

    def add_animal(self, animal):
        if isinstance(animal, Animal):
            self.animals.append(animal)

    def __str__(self):
        return f"Enclosure: {self.name}, Type: {self.enclosure_type}, Size: {self.size}, Animals: {[str(animal) for animal in self.animals]}"
