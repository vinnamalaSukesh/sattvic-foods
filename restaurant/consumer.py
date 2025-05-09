import json
from channels.generic.websocket import WebsocketConsumer,async_to_sync
class Menu(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.group_name = 'menu_updates'
        async_to_sync(self.channel_layer.group_add)(self.group_name, self.channel_name)

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(self.group_name, self.channel_name)

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        async_to_sync(self.channel_layer.group_send)(self.group_name, {
            'type': 'send_message',
            'message': message
        })

    def send_message(self, event):
        self.send(text_data=json.dumps({'message': event['message']}))

class Order(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.group_name = 'orders'
        async_to_sync(self.channel_layer.group_add)(self.group_name, self.channel_name)

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(self.group_name, self.channel_name)

    def receive(self, text_data):
        pass

    def send_message(self, event):
        self.send(text_data=json.dumps({'message': 'New order'}))