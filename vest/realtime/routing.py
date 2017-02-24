from channels import include
from channels.routing import route
import weather.consumers as wc

weather_routing = [
    route("websocket.connect", wc.ws_add),
    route("websocket.receive", wc.ws_message),
    route("websocket.disconnect", wc.ws_disconnect),
]

channel_routing = [
    include(weather_routing, path=r"^/weather"),
]
