from heroes import Warrior, Mage, Paladin
from inventory_decorator import InventoryDecorator

def main():
    warrior = Warrior("Conan")
    mage = Mage("Merlin")
    paladin = Paladin("Arthas")

    warrior_decorator = InventoryDecorator(warrior)
    mage_decorator = InventoryDecorator(mage)
    paladin_decorator = InventoryDecorator(paladin)

    warrior_decorator.add_item("Sword")
    warrior_decorator.add_item("Shield")
    mage_decorator.add_item("Staff")
    mage_decorator.add_item("Robe")
    paladin_decorator.add_item("Hammer")
    paladin_decorator.add_item("Armor")

    print(warrior_decorator.get_stats())
    print(mage_decorator.get_stats())
    print(paladin_decorator.get_stats())

if __name__ == "__main__":
    main()
