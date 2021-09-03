from Data import Data
from model.Balance import Balance


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

    def fetch(self, account_id):
        account_events = BalanceService(account_id).fetch_events()

        if len(account_events) == 0:
            return "0", 404

        account_balance = Balance(account_events, account_id)
        balance_int = int(account_balance.total)
        return str(balance_int), 200
