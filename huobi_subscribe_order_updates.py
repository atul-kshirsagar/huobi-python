import websocket
import json
import time
import hmac
import hashlib
import base64
import zlib 
from datetime import datetime
ACCESS_KEY = ""
SECRET_KEY = ""

def on_message(ws, message):
    # message = zlib.decompress(message, 16+zlib.MAX_WBITS)
    data = json.loads(message)
    print("received: ",data)
    if "ping" in data:
        # Respond to ping messages to keep the connection alive
        ws.send(json.dumps({"pong": data["ping"]}))
    elif "status" in data and data["status"] == "ok":
        # Handle successful authentication
        print("Authenticated successfully")
    elif "ch" in data and data["ch"].startswith("market.") and data["ch"].endswith(".trade.detail"):
        # Handle trade detail messages
        print(data)
    elif "action" in data and data["action"] == 'req':
        ws.send(json.dumps({
                            "action": "sub",
                            "ch": "orders#btcusdt"
                            }))
        print("sent subscription")

def on_error(ws, error):
    print("error: ",error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    # Generate the subscription message and sign it with the API key and secret key
    print("on open")
    timestamp = str(datetime.now()).replace(" ",'T')[:-7]
    timestampN = timestamp.replace(":","%3A")
    print(timestampN)
    paramsval = f"GET\napi.huobi.pro\n/ws/v2\naccessKey={ACCESS_KEY}&signatureMethod=HmacSHA256&signatureVersion=2.1&timestamp={timestampN}"
    print("param: ",paramsval)
    signature = hmac.new(SECRET_KEY.encode(), paramsval.encode(), digestmod=hashlib.sha256).digest()
    signature = base64.b64encode(signature).decode()
    send_jsonval = json.dumps({
    "action": "req", 
    "ch": "auth",
    "params": { 
        "authType":"api",
        "accessKey": ACCESS_KEY,
        "signatureMethod": "HmacSHA256",
        "signatureVersion": "2.1",
        "timestamp": timestamp,
        "signature": signature
    }})
    print(send_jsonval)
    ws.send(send_jsonval)

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://api.huobi.pro/ws/v2",
                              on_message=on_message,
                              on_error=on_error,
                              on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()
