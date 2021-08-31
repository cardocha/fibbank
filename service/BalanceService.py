from Data import Data
from model.Balance import Balance


class BalanceService:

    def __init__(self, account_id):
        self.account_id = account_id

    def fetch_as_json(self):
        account_events = Data().fetch_events(self.account_id)
        return Balance(account_events, self.account_id).json()
