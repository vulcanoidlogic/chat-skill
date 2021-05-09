from mycroft import MycroftSkill, intent_file_handler


class Chat(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('chat.intent')
    def handle_chat(self, message):
        self.speak_dialog('chat')


def create_skill():
    return Chat()

