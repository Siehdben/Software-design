from animal import Animal
from enclosure import Enclosure
from food import Food
from zooworker import ZooWorker
from inventory import Inventory

def main():
    # Create animals
    lion = Animal("Leo", "Lion", 5)
    tiger = Animal("Tigra", "Tiger", 3)

    # Create enclosures
    big_cat_enclosure = Enclosure("Big Cat Enclosure", "Outdoor", "Large")
    big_cat_enclosure.add_animal(lion)
    big_cat_enclosure.add_animal(tiger)

    # Create food
    meat = Food("Meat", 100)

    # Create zoo workers
    zookeeper = ZooWorker("Alice", "Zookeeper")
    veterinarian = ZooWorker("Bob", "Veterinarian")

    # Create inventory and add items
    zoo_inventory = Inventory()
    zoo_inventory.add_animal(lion)
    zoo_inventory.add_animal(tiger)
    zoo_inventory.add_enclosure(big_cat_enclosure)
    zoo_inventory.add_food(meat)
    zoo_inventory.add_worker(zookeeper)
    zoo_inventory.add_worker(veterinarian)

    # Display inventory
    zoo_inventory.display_inventory()

if __name__ == "__main__":
    main()
