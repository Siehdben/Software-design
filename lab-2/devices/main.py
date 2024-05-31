from factories import IProneFactory, KiaomiFactory, BalaxyFactory

def main():
    iprone_factory = IProneFactory()
    kiaomi_factory = KiaomiFactory()
    balaxy_factory = BalaxyFactory()

    devices = [
        iprone_factory.create_laptop(),
        kiaomi_factory.create_netbook(),
        balaxy_factory.create_ebook(),
        iprone_factory.create_smartphone()
    ]

    for device in devices:
        print(device)

if __name__ == "__main__":
    main()
