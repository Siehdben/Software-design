class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def __str__(self):
        return f"{self.brand} {self.model}"

class Laptop(Device):
    def __init__(self, brand):
        super().__init__(brand, "Laptop")

class Netbook(Device):
    def __init__(self, brand):
        super().__init__(brand, "Netbook")

class EBook(Device):
    def __init__(self, brand):
        super().__init__(brand, "EBook")

class Smartphone(Device):
    def __init__(self, brand):
        super().__init__(brand, "Smartphone")
