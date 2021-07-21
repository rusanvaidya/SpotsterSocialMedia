from django.conf.urls import url
from chatbox.consumers import chatConsumer

websocket_urlpatterns = [
    url(r'^ws/chatbox/(?P<room_code>\w+)/$', chatConsumer.as_asgi()),
]