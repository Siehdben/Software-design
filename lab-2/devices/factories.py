from devices import Laptop, Netbook, EBook, Smartphone

class DeviceFactory:
    def create_laptop(self):
        raise NotImplementedError

    def create_netbook(self):
        raise NotImplementedError

    def create_ebook(self):
        raise NotImplementedError

    def create_smartphone(self):
        raise NotImplementedError

class IProneFactory(DeviceFactory):
    def create_laptop(self):
        return Laptop("IProne")

    def create_netbook(self):
        return Netbook("IProne")

    def create_ebook(self):
        return EBook("IProne")

    def create_smartphone(self):
        return Smartphone("IProne")

class KiaomiFactory(DeviceFactory):
    def create_laptop(self):
        return Laptop("Kiaomi")

    def create_netbook(self):
        return Netbook("Kiaomi")

    def create_ebook(self):
        return EBook("Kiaomi")

    def create_smartphone(self):
        return Smartphone("Kiaomi")

class BalaxyFactory(DeviceFactory):
    def create_laptop(self):
        return Laptop("Balaxy")

    def create_netbook(self):
        return Netbook("Balaxy")

    def create_ebook(self):
        return EBook("Balaxy")

    def create_smartphone(self):
        return Smartphone("Balaxy")
