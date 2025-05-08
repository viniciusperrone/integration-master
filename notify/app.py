from flask import Flask, request, jsonify


app = Flask(__name__)

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
