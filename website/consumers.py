from channels.generic.websocket import WebsocketConsumer

class MyConsumer(WebsocketConsumer):
    groups = ["broadcast"]

    def connect(self):
        pass

    def receive(self, text_data=None, bytes_data=None):
        pass

    def disconnect(self, close_code):
        pass