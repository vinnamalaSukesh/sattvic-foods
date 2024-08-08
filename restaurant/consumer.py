import json
from channels.generic.websocket import WebsocketConsumer
from channels.db import database_sync_to_async
class Order(WebsocketConsumer):
    def connect(self):
        self.room_name = "Orders"
        self.channel_layer.group_add(self.room_name, self.channel_name)
        self.accept()

    def disconnect(self, close_code):
        self.channel_layer.group_discard(self.room_name, self.channel_name)

    def receive(self, text_data):
        pass
    def send_message(self, event):
        data = event['message']
        self.send(text_data=json.dumps(data))
        print('data = ',data)