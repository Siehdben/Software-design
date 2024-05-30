from animal import Animal
from enclosure import Enclosure
from food import Food
from zooworker import ZooWorker

class Inventory:
    def __init__(self):
        self.animals = []
        self.enclosures = []
        self.foods = []
        self.workers = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_enclosure(self, enclosure):
        self.enclosures.append(enclosure)

    def add_food(self, food):
        self.foods.append(food)

    def add_worker(self, worker):
        self.workers.append(worker)

    def display_inventory(self):
        print("Animals in Zoo:")
        for animal in self.animals:
            print(animal)

        print("\nEnclosures in Zoo:")
        for enclosure in self.enclosures:
            print(enclosure)

        print("\nFood Inventory:")
        for food in self.foods:
            print(food)

        print("\nZoo Workers:")
        for worker in self.workers:
            print(worker)
