import json

from Data import Data
from model.Balance import Balance
from model.Event import Event
from service.BalanceService import BalanceService


class EventService:
    def __init__(self, event_json):
        self.event_json = event_json

    def store(self):
        data = Data()
        new_event = self.parse()
        data.store(new_event)
        return new_event.destination

    def parse(self):
        return Event(self.event_json)

    def deposit(self):
        destination_account_id = EventService(self.event_json).store()
        destination_account_events = BalanceService(destination_account_id).fetch_events()
        account_balance = Balance(destination_account_events, destination_account_id)
        response = EventService.default_balance_response(destination_account_id, int(account_balance.total))
        return json.dumps({'destination': response}), 201

    def withdraw(self):
        origin_account_id = self.event_json['origin']
        origin_account_events = BalanceService(origin_account_id).fetch_events()

        if len(origin_account_events) == 0:
            return "0", 404

        EventService(self.event_json).store()
        origin_account_events = BalanceService(origin_account_id).fetch_events()
        account_balance = Balance(origin_account_events, origin_account_id)
        response = EventService.default_balance_response(origin_account_id, int(account_balance.total))
        return json.dumps({'origin': response}), 201

    def transfer(self):
        origin_account_id = self.event_json['origin']
        origin_account_events = BalanceService(origin_account_id).fetch_events()

        if len(origin_account_events) == 0:
            return "0", 404

        destination_account_id = self.event_json['destination']

        EventService(self.event_json).store()
        origin_account_events = BalanceService(origin_account_id).fetch_events()
        destination_account_events = BalanceService(destination_account_id).fetch_events()

        destination_account_balance = Balance(destination_account_events, destination_account_id)
        origin_account_balance = Balance(origin_account_events, origin_account_id)

        response_origin = EventService.default_balance_response(origin_account_id, int(origin_account_balance.total))
        response_destination = EventService.default_balance_response(destination_account_id,
                                                                     int(destination_account_balance.total))
        return json.dumps({'origin': response_origin, 'destination': response_destination}), 201

    @staticmethod
    def default_balance_response(account_id, balance):
        return {"id": account_id, "balance": balance}
