class Event:
    def __init__(self, json):
        self.type = json['type']
        self.origin = Event.optional_field(json, 'origin')
        self.destination = Event.optional_field(json, 'destination')
        self.amount = json['amount']

    def to_file_line(self):
        return "{},{},{},{}\r\n".format(self.type, self.origin, self.destination, self.amount)

    @staticmethod
    def optional_field(json, field):
        if field in json:
            return json[field]
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
