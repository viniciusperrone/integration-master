from flask import Flask, request, jsonify

from config.mongo import mongo


app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/notify"

mongo.init_app(app)

@app.route('/order/webhook', methods=['POST'])
def order_webhook():
    data = request.json

    print('data', data)

    return jsonify({'status': 'success'}), 200

if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )
