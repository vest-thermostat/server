from channels import include
from channels.routing import route
import weather.consumers as wc
import location.consumers as lc

weather_routing = [
    route("websocket.connect", wc.ws_add),
    route("websocket.receive", wc.ws_message),
    route("websocket.disconnect", wc.ws_disconnect),
]

location_routing = [
    route("websocket.connect", lc.ws_add),
    route("websocket.receive", lc.ws_message),
    route("websocket.disconnect", lc.ws_disconnect),
]

channel_routing = [
    include(weather_routing, path=r"^/weather"),
    include(location_routing, path=r"^/location"),
]
