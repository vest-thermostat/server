from channels.routing import route
from . import consumers

channel_routing = {
    'websocket.connect': consumers.ws_add,
    'websocket.receive': consumers.ws_message,
    'websocket.disconnect': consumers.ws_disconnect,
}
