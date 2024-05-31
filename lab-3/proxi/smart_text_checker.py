from smart_text_reader import SmartTextReader

class SmartTextChecker:
    def __init__(self, filename):
        self.reader = SmartTextReader(filename)

    def read(self):
        print("Opening file...")
        content = self.reader.read()
        print("File read successfully!")
        print(f"Total lines: {len(content)}")
        print(f"Total characters: {sum(len(line) for line in content)}")
        return content
