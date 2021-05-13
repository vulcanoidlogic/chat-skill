import time
import requests
import json
import sys
import logging
from mycroft import MycroftSkill, intent_handler
from adapt.intent import IntentBuilder
from mycroft.util.parse import match_one
# from signalrcore.hub_connection_builder import HubConnectionBuilder

class Chat(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    # def initialize(self):
    #     chatHubUrl = "https://iobtweb.azurewebsites.net/chatHub"
    #     self.hub_connection = HubConnectionBuilder()\
    #         .with_url(chatHubUrl)\
    #             .configure_logging(logging.DEBUG)\
    #             .with_automatic_reconnect({
    #             "type": "raw",
    #             "keep_alive_interval": 60,
    #             "reconnect_interval": 30,
    #             "max_attempts": 5
    #         }).build()
    #     self.hub_connection.on("ChatMessage", self.handle_receive_message)
    #     self.hub_connection.start()

    @intent_handler(IntentBuilder("")
                    .require("ChatKeyword").require("text"))
    def handle_chat(self, message):
        text = message.data.get("text")
        self.post_message(text)
        # self.send_message(text)

    # def send_message(self, text):
    #     message = dict({
    #         "user": "Llam_9",
    #         "message": text,
    #         "sourceGuid": "375ad623-6e7c-4272-8aa7-d631d22a356d",
    #         "timeStamp": "2021-04-07T11:55:46.669Z",
    #         "personId": "Llam_9"
    #       })
    #     self.hub_connection.send("ChatMessage", [message])

    def post_message(self, text):
        message = dict({
            "user": "Llam_9",
            "message": text,
            "sourceGuid": "375ad623-6e7c-4272-8aa7-d631d22a356d",
            "timeStamp": "2021-04-07T11:55:46.669Z",
            "personId": "Llam_9"
          })
        # chatURL = "https://192.168.1.20:5000/api/ChatHub/ChatMessage"
        chatURL = "https://iobtweb.azurewebsites.net/api/ChatHub/ChatMessage"
        # chatURL = "http://localhost:5000/api/ChatHub/ChatMessage"
        headers = dict({'Content-type':'application/json', 'Accept':'application/json'})
        response = requests.post(url = chatURL, json = message, headers = headers)
        result = response.json()
        self.speak_dialog('chat')
        #print(result)
        if ( result['hasError'] == True):
            print(result['message'])
        else:
            payload = result['payload']
            print(payload)

    # def handle_receive_message(self, payload):
    #     self.speak_dialog("Incoming Message")
    #     self.speak_dialog(payload[0]["message"])

    # def stop(self):
    #     if (self.hub_connection):
    #         self.hub_connection.stop()

    # def shutdown(self):
    #     if (self.hub_connection):
    #         self.hub_connection.stop()

def create_skill():
    return Chat()

