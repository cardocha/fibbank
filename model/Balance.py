class Balance:
    def __init__(self, events, destination):
        self.destination = destination
        self.events = events
        self.total = self.calculate()

    def calculate(self):
        total = 0.0
        for event in self.events:
            total += float(event.amount)
        return total

    def json(self):
        return {"destination": {"id": self.destination, "balance": str(self.total)}}
