from Data import Data


class BalanceService:

    def __init__(self, account_id):
        self.account_id = account_id

    def fetch_events(self):
        events = Data().fetch_events()
        account_events = []

        for event in events:
            if event.destination == self.account_id or event.origin == self.account_id:
                account_events.append(event)

        return account_events
