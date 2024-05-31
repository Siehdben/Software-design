class Logger:
    def log(self, message):
        print(f"\033[92m{message}\033[0m")  # Green text

    def error(self, message):
        print(f"\033[91m{message}\033[0m")  # Red text

    def warn(self, message):
        print(f"\033[93m{message}\033[0m")  # Orange text
