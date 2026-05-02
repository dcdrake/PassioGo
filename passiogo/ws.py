import json

import websocket


def launch_ws():
    uri = "wss://passio3.com/"

    websocket.enableTrace(False)
    wsapp = websocket.WebSocketApp(
        uri,
        on_open=subscribe_ws,
        on_error=handle_ws_error,
        on_close=handle_ws_close,
    )
    wsapp.run_forever(ping_interval=5, ping_timeout=3)


def handle_ws_error(wsapp, error): ...


def handle_ws_close(wsapp, close_status_code, close_msg):
    wsapp.close()


def subscribe_ws(wsapp, user_id):
    subscription_msg = {
        "subscribe": "location",
        "userId": [user_id],
        "field": ["busId", "latitude", "longitude", "course", "paxLoad", "more"],
    }
    wsapp.send(json.dumps(subscription_msg))
