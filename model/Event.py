from model.EventType import EventType


class Event:
    def __init__(self, json):
        self.type = json['type']
        self.origin = Event.find_origin(json)
        self.destination = json['destination']
        self.amount = json['amount']
        self.update_amount()

    def update_amount(self):
        if self.type == EventType.WITHDRAW:
            self.amount = -self.amount

    def to_file_line(self):
        return "{},{},{},{}\r\n".format(self.type, self.origin, self.destination, self.amount)

    @staticmethod
    def find_origin(json):
        if 'origin' in json:
            return json['origin']
        return 0

    @staticmethod
    def from_file_line(line):
        fields = line.split(',')
        json_line = {
            'type': fields[0],
            'origin': fields[1],
            'destination': fields[2],
            'amount': fields[3]
        }
        return Event(json_line)
