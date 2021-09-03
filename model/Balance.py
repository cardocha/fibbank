class Balance:
    def __init__(self, events, account_id):
        self.account_id = account_id
        self.events = events
        self.total = 0.0
        self.calculate()

    def calculate(self):
        for event in self.events:
            self.sum(event)

    def sum(self, event):
        value = float(event.amount)
        print(event.type == 'withdraw')
        if event.type == 'withdraw' or (event.type == 'transfer' and event.origin == self.account_id):
            self.total -= value
        else:
            self.total += value

        if event == 'transfer' and event.destination == self.account_id:
            self.total += value
