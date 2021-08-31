from Data import Data
from model.Event import Event


class EventService:
    def __init__(self, event_json):
        self.event_json = event_json

    def store(self):
        data = Data()
        new_event = Event(self.event_json)
        data.store(new_event)
        return new_event.destination
