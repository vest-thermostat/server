from channels import include
from channels.routing import route
import weather.consumers as wc
import location.consumers as lc
import home.consumers as hc

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

home_routing = [
    route("websocket.connect", hc.ws_add),
    route("websocket.receive", hc.ws_message),
    route("websocket.disconnect", hc.ws_disconnect),
]

channel_routing = [
    include(weather_routing, path=r"^/ws/weather"),
    include(location_routing, path=r"^/ws/location"),
    include(home_routing, path=r"^/ws/home"),
]
