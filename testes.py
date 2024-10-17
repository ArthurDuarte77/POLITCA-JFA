import requests
import time
# requests.post("http://localhost:300/api/sendText", json={
#     "session": "default",
#     "chatId": "553784087335@c.us",
#     "text": "Hi there!"
# })

while True:
    time.sleep(1)
    requests.post("http://localhost:3000/api/sendText", json={
    "chatId": "553784087335@c.us",
    "text": """CAIO ESTAMOS EM CALL TE ESPERANDO!!!!""",
    "session": "default"
    })
        