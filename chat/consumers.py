from channels.consumer import AsyncConsumer, SyncConsumer
from channels.db import database_sync_to_async
from asgiref.sync import async_to_sync,sync_to_async
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from chat.models import Thread, Message

import json

from core.models.channel_models import Channel

from channels.layers import get_channel_layer

from asgiref.sync import async_to_sync

import sys

User = get_user_model()

from chat.buffer_handler import RoomConsumerCount

class ChatConsumer(AsyncConsumer):
    async def websocket_connect(self,event):
        # print(self.scope.keys())
        me = self.scope['user']
        self.other_username = self.scope['url_route']['kwargs']['username']
        self.other_user = await sync_to_async(User.objects.get)(id = self.other_username)
        self.thread_obj = await sync_to_async(Thread.objects.get_or_create_personal_thread)(me,self.other_user)
        self.room_name = f'personal_thread_{self.thread_obj.id}'

        # print(self.room_name)

        await self.channel_layer.group_add(self.room_name,self.channel_name)
        await self.send({
            'type':'websocket.accept'
        })
        # print(f'[{self.channel_name}] - you are connected')
        try:
            RoomConsumerCount[self.room_name] = RoomConsumerCount[self.room_name]+1
        except:
            RoomConsumerCount[self.room_name] = 1
        # print("room_consumer_count", RoomConsumerCount)

    async def websocket_receive(self,event):
        # print(f'[{self.channel_name}] - Receive message - {event["text"]}')

        msg = json.dumps({
            'text':event.get('text'),
            'username':self.scope['user'].username,
            'sender_id':self.scope['user'].id,
            'receiver_id':self.other_user.id
        })

        # channel_layer1 = get_channel_layer()
        # ch_group_list = channel_layer1.group_channels(self.room_name)
        # print("channel group list ", ch_group_list)
        
        # print("user count",len(self.channel_layer.groups.get(self.room_name, {}).items()))

        await self.store_message(event.get('text'), RoomConsumerCount[self.room_name])
        await self.send_new_message_notification(self.other_username)

        await self.channel_layer.group_send(
            self.room_name,
            {
            'type':'websocket.message',
            'text':msg
        })

    async def websocket_message(self,event):
        # print(f'[{self.channel_name}] - Message sent -{event["text"]}')
        await self.send({
            'type':'websocket.send',
            'text':event.get('text')
        })

    async def websocket_disconnect(self,event):
        # print(f'[{self.channel_name}] - Disconnected')
        await self.channel_layer.group_discard(self.room_name,self.channel_name)
        if RoomConsumerCount[self.room_name] == 2:
            RoomConsumerCount[self.room_name] = 1
        else:
            del(RoomConsumerCount[self.room_name])
        # print("room_consumer_count_disconnect", RoomConsumerCount)

    @database_sync_to_async
    def store_message(self,text, consumer_count):
        try:
            if consumer_count == 2:
                Message.objects.create(
                    thread = self.thread_obj,
                    sender = self.scope['user'],
                    text = text,
                    is_seen = True
                )
            elif consumer_count == 1:
                Message.objects.create(
                    thread = self.thread_obj,
                    sender = self.scope['user'],
                    text = text
                )
        except:
            Message.objects.create(
                    thread = self.thread_obj,
                    sender = self.scope['user'],
                    text = text
                )

    @database_sync_to_async
    def send_new_message_notification(self,other_username):
        # print("---send_new_message_notification---")
        # print(other_username)
        try:
            # user_id = Channel.objects.filter(user_id=other_username)[0]
            # print("from send notification",user_id)
            channel_layer = get_channel_layer()
            channel = Channel.objects.get(user_id = other_username)
            async_to_sync(channel_layer.group_send)(
            channel.group_name,{
                'type':'websocket.message',
                'text':"new mesage received"
                }
        )
        except:
            #receiver is not online
            # print(sys.exc_info())
            pass

# class EchoConsumer(SyncConsumer):
#     def websocket_connect(self,event):
#         self.room_name = 'broadcast'

#         self.send({
#             'type':'websocket.accept'
#         })

#         async_to_sync(self.channel_layer.group_add)(self.room_name,self.channel_name)
#         print(f'[{self.channel_name}] - you are connected')

#     def websocket_receive(self,event):
#         print(f'[{self.channel_name}] - Receive message - {event["text"]}')
#         async_to_sync(self.channel_layer.group_send)(
#             self.room_name,
#             {
#             'type':'websocket.message',
#             'text':event.get('text')
#         })

#     def websocket_message(self,event):
#         print(f'[{self.channel_name}] - Message sent -{event["text"]}')
#         self.send({
#             'type':'websocket.send',
#             'text':event.get('text')
#         })

#     def websocket_disconnect(self,event):
#         print(f'[{self.channel_name}] - Disconnected')
#         async_to_sync(self.channel_layer.group_discard)(self.room_name,self.channel_name)