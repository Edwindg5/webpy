#tutorial/routingsocket.py
from django.urls import re_path
from tutorial.consumers import CarreraConsumer, ProfesorConsumer

websocket_urlpatterns = [
    re_path(r"ws/about/$", CarreraConsumer.as_asgi()),
    re_path(r"ws/profesores/$", ProfesorConsumer.as_asgi()),  # Nueva ruta para profesores
]
