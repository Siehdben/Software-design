from singleton import Authenticator

def main():
    auth1 = Authenticator()
    auth2 = Authenticator()

    auth1.authenticate("Alice")
    auth2.authenticate("Bob")
    auth1.authenticate("Alice")

    print(auth1)
    print(auth2)

    print(auth1 is auth2)  # Should print True

if __name__ == "__main__":
    main()
