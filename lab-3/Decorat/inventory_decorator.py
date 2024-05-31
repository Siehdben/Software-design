class InventoryDecorator:
    def __init__(self, hero):
        self.hero = hero

    def add_item(self, item):
        self.hero.inventory.append(item)

    def get_stats(self):
        return self.hero.get_stats()
