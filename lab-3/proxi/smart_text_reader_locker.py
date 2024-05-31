import re
from smart_text_reader import SmartTextReader

class SmartTextReaderLocker:
    def __init__(self, filename, pattern):
        self.reader = SmartTextReader(filename)
        self.pattern = pattern

    def read(self):
        if re.match(self.pattern, self.reader.filename):
            print("Access denied!")
            return None
        else:
            return self.reader.read()
