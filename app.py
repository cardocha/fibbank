from flask import Flask, request

from Data import Data
from service.BalanceService import BalanceService
from service.EventService import EventService

app = Flask(__name__)


@app.route("/reset", methods=['POST'])
def reset():
    Data().clear()
    return "OK", 200


@app.route("/event", methods=['POST'])
def event():
    json_request = request.get_json()
    if json_request['type'] == 'deposit':
        return EventService(json_request).deposit()

    if json_request['type'] == 'withdraw':
        return EventService(json_request).withdraw()

    if json_request['type'] == 'transfer':
        return EventService(json_request).transfer()


@app.route("/balance", methods=['GET'])
def balance():
    account_id = request.args.get("account_id")
    return BalanceService(account_id).fetch()
