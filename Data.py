from model.EventType import EventType


class Data:
    def __init__(self):
        self.file = None

    def clear(self):
        self.file = open('data.fib', 'w', encoding="utf-8")
        self.file.close()

    def store(self, event):
        self.file = open('data.fib', 'a', encoding="utf-8")
        self.file.write(event.to_file_line())
        self.file.close()
