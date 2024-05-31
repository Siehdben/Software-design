class SmartTextReader:
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename, 'r') as f:
            return [list(line) for line in f.readlines()]
