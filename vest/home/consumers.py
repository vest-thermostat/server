from channels import Group
from channels.sessions import channel_session
from channels.auth import http_session_user, channel_session_user, channel_session_user_from_http
import json

@channel_session_user_from_http
def ws_add(message):
    # Accept connection
    message.reply_channel.send({"text": json.dumps({
        "accept": True,
        "user": message.user.username,
    })})
    # Add them to the right group
    Group("home-%s" % message.user.username).add(message.reply_channel)

# Connected to websocket.receive
@channel_session_user
def ws_message(message):
    Group("home-%s" % message.user.username).send({
        "text": message['text'],
    })

# Connected to websocket.disconnect
@channel_session_user
def ws_disconnect(message):
    Group("home-%s" % message.user.username).discard(message.reply_channel)
