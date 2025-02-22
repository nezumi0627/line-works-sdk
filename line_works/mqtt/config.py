from line_works.config import UA

HOST = "wss://jp1-web-noti.worksmobile.com/wmqtt"
HEADERS = {
    "user-agent": UA,
    "origin": "https://talk.worksmobile.com",
    "sec-websocket-protocol": "mqtt",
}
# MQTT接続設定
KEEPALIVE_INTERVAL_SEC = 50  # キープアライブ間隔(ms)
PROTOCOL_NAME = "MQTT"  # プロトコル名
PROTOCOL_LEVEL = 0x04  # MQTT v3.1.1(内部実装に基づく)
KEEP_ALIVE = 0x32  # 50秒(内部実装に基づく)
