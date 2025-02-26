#tutorial/routingsocket.py
from django.urls import path
from .consumers import MyConsumer # type: ignore

websocket_urlpatterns = [
    path('ws/somepath/', MyConsumer.as_asgi()),
]
