from model.Event import Event


class Data:
    def __init__(self):
        self.file = None

    def open_file(self, mode):
        self.file = open('data.fib', mode, encoding="utf-8")

    def clear(self):
        self.open_file('w')
        self.file.close()

    def store(self, event):
        self.open_file('a')
        self.file.write(event.to_file_line())
        self.file.close()

    def fetch_events(self, destination):
        events = []
        self.open_file('r')
        for line in self.file:
            line_fields = line.split(',')
            event = Event(line_fields)
            if event.destination == destination:
                events.append(event)
        self.file.close()
        return events
