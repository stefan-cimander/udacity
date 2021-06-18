from flask import Flask, jsonify, request

from .services import create_order, retrieve_orders

app = Flask(__name__)


@app.route('/health', methods=['GET'])
def health():
    return jsonify({'result': 'Hello, World!'})


@app.route('/api/orders', methods=['POST'])
def create():
    created_order = create_order(request.json)
    return jsonify(created_order)


@app.route('/api/orders', methods=['GET'])
def getAll():
    orders = retrieve_orders()
    return jsonify(orders)


if __name__ == '__main__':
    app.run()
