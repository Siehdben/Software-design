class HeroBuilder:
    def __init__(self):
        self.hero = Hero()

    def set_height(self, height):
        self.hero.height = height
        return self

    def set_body_type(self, body_type):
        self.hero.body_type = body_type
        return self

    def set_hair_color(self, hair_color):
        self.hero.hair_color = hair_color
        return self

    def set_eye_color(self, eye_color):
        self.hero.eye_color = eye_color
        return self

    def set_clothing(self, clothing):
        self.hero.clothing = clothing
        return self

    def set_inventory(self, inventory):
        self.hero.inventory = inventory
        return self

    def build(self):
        return self.hero

class Hero:
    def __init__(self):
        self.height = None
        self.body_type = None
        self.hair_color = None
        self.eye_color = None
        self.clothing = None
        self.inventory = None

    def __str__(self):
        return f"Hero(height={self.height}, body_type={self.body_type}, hair_color={self.hair_color}, eye_color={self.eye_color}, clothing={self.clothing}, inventory={self.inventory})"

class EnemyBuilder(HeroBuilder):
    def __init__(self):
        super().__init__()
        self.hero = Hero()  # This will actually be an Enemy

    def set_evil_plan(self, evil_plan):
        self.hero.evil_plan = evil_plan
        return self

    def build(self):
        return self.hero

class Enemy(Hero):
    def __init__(self):
        super().__init__()
        self.evil_plan = None

    def __str__(self):
        return f"Enemy(height={self.height}, body_type={self.body_type}, hair_color={self.hair_color}, eye_color={self.eye_color}, clothing={self.clothing}, inventory={self.inventory}, evil_plan={self.evil_plan})"
