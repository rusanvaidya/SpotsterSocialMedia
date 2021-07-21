import json

from django.core.checks import messages
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from chatbox.models import usermessages

class chatConsumer(AsyncJsonWebsocketConsumer):
    
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_code']
        # print(self.room_name)
        self.room_group_name = 'room_%s' % self.room_name
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
    
    async def receive(self, text_data):
        response = json.loads(text_data)
        event = response.get("event", None)
        message = response.get("message", None)
        
        if event == 'listen':
            await self.channel_layer.group_send(self.room_group_name, {
                'type': 'send_message',
                'message': message,
                "event": "listen"
            })
            if message != None:
                if message['room_code'] != 'asd123123':
                    chat_id = int(message['cid'])
                    msg_text = message['text']
                    active_id = int(message['user_id'])
                    room_codes = message['room_code']

                    stor_msg = usermessages(messgd = msg_text, activeuser = active_id, roomcode = room_codes,chatid = chat_id)
                    stor_msg.save()

        if event == 'wait':
            await self.channel_layer.group_send(self.room_group_name, {
                'type': 'send_message',
                'message': message,
                'event': "wait"
            })

    async def send_message(self, res):
        await self.send(text_data=json.dumps({
            "payload": res,
        }))