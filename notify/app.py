import json
from flask import Flask, request, jsonify

from config.mongo import mongo


app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://mongodb:27017/notify"

mongo.init_app(app)

mongo.db.orders.create_index([('event_type', 'text'), ('event', 'text')])

from models import NotifyOrderModel


@app.route('/order/webhook', methods=['POST'])
def order_webhook():
    data = request.json

    NotifyOrderModel.create_notify_order(
        event_type=data.get('event_type'),
        event=json.dumps(data, ensure_ascii=False),
    )

    return jsonify({
        'status': 'success',
        'data': data
    }), 200

if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )
