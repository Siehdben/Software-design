import threading

class SingletonMeta(type):
    _instances = {}
    _lock: threading.Lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]

class Authenticator(metaclass=SingletonMeta):
    def __init__(self):
        if hasattr(self, "_initialized"):
            return
        self._initialized = True
        self.authenticated_users = []

    def authenticate(self, user):
        if user not in self.authenticated_users:
            self.authenticated_users.append(user)
            print(f"User {user} authenticated.")
        else:
            print(f"User {user} already authenticated.")

    def __str__(self):
        return f"Authenticator(users={self.authenticated_users})"
