from logger import Logger
from file_writer import FileWriter

class FileLoggerAdapter:
    def __init__(self, file_writer):
        self.file_writer = file_writer

    def log(self, message):
        self.file_writer.write_line(f"LOG: {message}")

    def error(self, message):
        self.file_writer.write_line(f"ERROR: {message}")

    def warn(self, message):
        self.file_writer.write_line(f"WARN: {message}")
