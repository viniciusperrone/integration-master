import os
import json
from flask import Flask, request, jsonify
from dotenv import load_dotenv


from config.mongo import mongo
from services.callmebot import CallMeBotService
from services.email import DispatchEmail
from utils.message import outflow_event_message

load_dotenv()

app = Flask(__name__)

app.config["MONGO_URI"] = os.getenv("MONGO_URI", "mongodb://mongodb:27017/notify")

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

    product_name = data.get('product')
    quantity = data.get('quantity')
    product_cost_price = data.get('product_cost_price')
    product_selling_price = data.get('product_selling_price')
    total_value = product_selling_price * quantity
    profit_value = total_value - (product_cost_price * quantity)

    message = outflow_event_message.format(
        product_name,
        quantity,
        total_value,
        profit_value
    )

    callmebot = CallMeBotService()
    dispatch_email = DispatchEmail()

    callmebot.send_message(message)
    dispatch_email.send_email(
        subject='Nova Saída (SGE)',
        body=message,
        recipient_email='perronevinicius2018@gmail.com'
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
