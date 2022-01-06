import flask
from flask import request, jsonify
from flask_cors import CORS
import json
import sys

app = flask.Flask(__name__)
CORS(app)

@app.route('/dapr/subscribe', methods=['GET'])
def subscribe():
    subscriptions = [{'pubsubname': 'pubsub', 'topic': 'order', 'route': 'order'}, {'pubsubname': 'pubsub', 'topic': 'cart', 'route': 'cart'}]
    return jsonify(subscriptions)

@app.route('/order', methods=['POST'])
def a_subscriber():
    print(f'Order: {request.json}', flush=True)
    print('Order_Subscriber Received message "{}" on topic "{}"'.format(request.json['data']['message'], request.json['topic']), flush=True)
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 

@app.route('/cart', methods=['POST'])
def c_subscriber():
    print(f'Cart: {request.json}', flush=True)
    print(' Cart_Subscriber Received message "{}" on topic "{}"'.format(request.json['data']['message'], request.json['topic']), flush=True)
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 

app.run()
