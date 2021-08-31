from model.EventType import EventType


class Event:
    def __init__(self, json):
        self.type = json['type']
        self.origin = json['origin']
        self.destination = json['destination']
        self.amount = json['amount']
        self.update_amount()

    def __init__(self, fields):
        self.type = fields[0]
        self.origin = fields[1]
        self.destination = fields[2]
        self.amount = fields[3]
        self.update_amount()

    def update_amount(self):
        if self.type == EventType.WITHDRAW:
            self.amount = -self.amount

    def to_file_line(self):
        return "{},{},{},{}\r\n".format(self.type, self.origin, self.destination, self.amount)
