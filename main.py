from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("Received Webhook Data:", data)

    entry = data.get("entry")
    stoploss = data.get("stoploss")
    takeprofit = data.get("takeprofit")

    # Here: You can call your exchange API
    print(f"Entry: {entry}, SL: {stoploss}, TP: {takeprofit}")

    return jsonify({"status": "received", "entry": entry}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
    
