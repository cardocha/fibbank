from flask import Flask, request

from Data import Data
from model.Balance import Balance
from model.Event import Event

app = Flask(__name__)


@app.route("/reset", methods=['POST'])
def reset():
    Data().clear()
    return "", 200


@app.route("/event", methods=['POST'])
def event():
    new_event = Event(request.get_json())
    account_id = new_event.destination
    data = Data()
    data.store(new_event)
    account_events = data.fetch_events(account_id)
    return Balance(account_events, account_id).json(), 201


@app.route("/balance", methods=['GET'])
def balance():
    account_id = request.form['account_id']
    account_events = Data().fetch_events(account_id)
    return Balance(account_events, account_id)
