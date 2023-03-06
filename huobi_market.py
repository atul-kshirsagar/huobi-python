import json
from datetime import datetime, timezone
import websocket
import gzip

url = "wss://api.huobi.pro/ws"

def on_message(ws, message):
    data = json.loads(gzip.decompress(message))
    print("data : ",data)
    #print("message: ",message)

def on_error(ws, error):
    print(error)

def on_close(ws,temp1,temp2):
    print("WebSocket closed",temp1,temp2)

def on_open(ws):
    print("WebSocket opened")
    ws.send(json.dumps({
        "sub": "market.btcusdt.ticker"
    }))

ws = websocket.WebSocketApp(
    url,
    on_message=on_message,
    on_error=on_error,
    on_close=on_close
    )
ws.on_open = on_open
ws.run_forever()