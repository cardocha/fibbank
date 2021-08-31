class Balance:
    def __init__(self, events, destination):
        self.destination = destination
        self.events = events

    def json(self):
        destination_balance = 0
        for event in self.events:
            destination_balance += event.amount
        return {"destination": {"id": self.destination, "balance": destination_balance}}
