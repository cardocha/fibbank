from flask import Flask, request

from Data import Data
from model.Event import Event

app = Flask(__name__)


@app.route("/reset", methods=['POST'])
def reset():
    Data().clear()
    return "", 200


@app.route("/event", methods=['POST'])
def event():
    new_event = Event(request.get_json())
    Data().store(new_event)
    return {"destination": {"id": event.destination, "balance": 10}}, 201


@app.route("/balance", methods=['GET'])
def balance():
    return ''
