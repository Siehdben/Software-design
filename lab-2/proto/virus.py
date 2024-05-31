import copy

class Virus:
    def __init__(self, name, species, weight, age):
        self.name = name
        self.species = species
        self.weight = weight
        self.age = age
        self.children = []

    def clone(self):
        cloned_virus = copy.deepcopy(self)
        return cloned_virus

    def add_child(self, child):
        self.children.append(child)

    def __str__(self):
        return f"Virus(name={self.name}, species={self.species}, weight={self.weight}, age={self.age}, children={len(self.children)})"
