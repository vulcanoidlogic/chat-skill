import json
import logging
import sys
from signalrcore.hub_connection_builder import HubConnectionBuilder

#https://github.com/mandrewcito/signalrcore

def received_message(message):
    print(f'in received message {message[0]["message"]}.')

chatHubUrl = "https://iobtweb.azurewebsites.net/chatHub"
hub_connection = HubConnectionBuilder()\
    .with_url(chatHubUrl)\
    .configure_logging(logging.DEBUG)\
    .with_automatic_reconnect({
        "type": "raw",
        "keep_alive_interval": 10,
        "reconnect_interval": 5,
        "max_attempts": 5
    }).build()

hub_connection.on_open(lambda: print("connection opened and handshake received ready to send messages"))
hub_connection.on_close(lambda: print("connection closed"))

hub_connection.on("ChatMessage", received_message)

hub_connection.start()

text = None

while text != "exit()":
    text = input(">> ")
    message = dict({
        "user": "Llam_9",
        "message": text,
        "sourceGuid": "375ad623-6e7c-4272-8aa7-d631d22a356d",
        "timeStamp": "2021-04-07T11:55:46.669Z",
        "personId": "Llam_9"
        })
    if text is not None and text != "" and text != "exit()":
        hub_connection.send("ChatMessage", [message])


hub_connection.stop()

sys.exit(0)