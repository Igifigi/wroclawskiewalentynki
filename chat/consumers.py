import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from .models import ChatMessage, Thread
from .utils import get_thread_name

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        user1_id = self.scope['user'].id
        user2_id = self.scope['url_route']['kwargs']['id']
        
        self.room_group_name = get_thread_name(user1_id, user2_id)
        
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        
        await self.accept()

    async def disconnect(self, code):
        self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_layer
        )

    async def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        message = data['message']
        username = data['username']
        user_full_name = data['user_full_name']
        
        await self.save_message(username, self.room_group_name, message)
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username,
                'user_full_name': user_full_name,
            }
        )
        
    async def chat_message(self, event):
        message = event['message']
        username = event['username']
        user_full_name = event['user_full_name']
        
        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
            'user_full_name': user_full_name,
        }))
    
    @database_sync_to_async
    def save_message(self, username, thread_name, message):
        ChatMessage.objects.create(
            sender=get_object_or_404(User, username=username),
            thread=get_object_or_404(Thread, name=thread_name),
            message=message
        )


