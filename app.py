from flask import Flask, request

from Data import Data
from model.Event import Event
from service.BalanceService import BalanceService
from service.EventService import EventService

app = Flask(__name__)


@app.route("/reset", methods=['POST'])
def reset():
    Data().clear()
    return "", 200


@app.route("/event", methods=['POST'])
def event():
    account_id = EventService(request.get_json()).store()
    return BalanceService(account_id).fetch_as_json(), 201


@app.route("/balance", methods=['GET'])
def balance():
    return BalanceService(request.form['account_id']).fetch_as_json(), 201
