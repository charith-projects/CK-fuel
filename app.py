from flask import Flask, jsonify

app = Flask(__name__)

PRICES = {"petrol": 95.5, "diesel": 88.2}


@app.route("/price/<fuel>")
def price(fuel):
    if fuel not in PRICES:
        return jsonify(error="unknown fuel"), 404
    return jsonify(fuel=fuel, price=PRICES[fuel])
