from smart_text_checker import SmartTextChecker
from smart_text_reader_locker import SmartTextReaderLocker

def main():
    filename = "sample.txt"
    checker = SmartTextChecker(filename)
    content = checker.read()
    print(content)

    locker = SmartTextReaderLocker(filename, r'.*secret.*')
    content = locker.read()
    print(content)

if __name__ == "__main__":
    main()
