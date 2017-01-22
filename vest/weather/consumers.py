from channels import Group
from channels.sessions import channel_session
from channels.auth import http_session_user, channel_session_user, channel_session_user_from_http
from .models import PrivateWeather
import json

# @channel_session
# def ws_connect(message):
#     prefix, token = message['weather'].strip('/').split('/')
#     weathers = PrivateWeather.objects.all()
#     # Group('weather-' + str(token)).add(message.reply_channel)
#     message.channel_session['weathers'] = weathers

# def msg_consumer(message):
#     # Save to model
#     room = message.content['room']
#     ChatMessage.objects.create(
#         room=room,
#         message=message.content['message'],
#     )
#     # Broadcast to listening sockets
#     Group("chat-%s" % room).send({
#         "text": message.content['message'],
#     })

@channel_session_user_from_http
def ws_add(message):
    # Accept connection
    message.reply_channel.send({"text": json.dumps({"accept": True})})
    # Add them to the right group
    Group("weather-%s" % message.user.username).add(message.reply_channel)

# Connected to websocket.receive
@channel_session_user
def ws_message(message):
    Group("weather-%s" % message.user.username).send({
        "text": message['text'],
    })

# Connected to websocket.disconnect
@channel_session_user
def ws_disconnect(message):
    Group("weather-%s" % message.user.username).discard(message.reply_channel)
