from logger import Logger
from file_writer import FileWriter
from file_logger_adapter import FileLoggerAdapter

def main():
    console_logger = Logger()
    file_writer = FileWriter("log.txt")
    file_logger = FileLoggerAdapter(file_writer)

    console_logger.log("This is a log message.")
    console_logger.error("This is an error message.")
    console_logger.warn("This is a warning message.")

    file_logger.log("This is a log message.")
    file_logger.error("This is an error message.")
    file_logger.warn("This is a warning message.")

if __name__ == "__main__":
    main()
