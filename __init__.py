import time
import requests
import json
import sys
from mycroft import MycroftSkill, intent_handler
from adapt.intent import IntentBuilder
from mycroft.util.parse import match_one


class Chat(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_handler(IntentBuilder("")
                    .require("ChatKeyword").require("text"))
    def handle_chat(self, message):
        text = message.data.get("text")
        # time.sleep(2)
        self.post_message(text)

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



def create_skill():
    return Chat()

