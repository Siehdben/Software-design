class Hero:
    def __init__(self, name):
        self.name = name
        self.inventory = []

    def get_stats(self):
        stats = f"{self.name} has the following inventory:\n"
        for item in self.inventory:
            stats += f"- {item}\n"
        return stats

class Warrior(Hero):
    def __init__(self, name):
        super().__init__(name)

class Mage(Hero):
    def __init__(self, name):
        super().__init__(name)

class Paladin(Hero):
    def __init__(self, name):
        super().__init__(name)
