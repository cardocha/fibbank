from model.EventType import EventType


class Event:
    def __init__(self, json):
        self.type = event_type
        self.origin = origin
        self.destination = destination
        self.amount = amount
        self.update_amount()

    def update_amount(self):
        if self.type == EventType.WITHDRAW:
            self.amount = -self.amount

    def to_file_line(self):
        return "{},{},{},{}\r\n".format(self.type, self.origin, self.destination, self.amount)
