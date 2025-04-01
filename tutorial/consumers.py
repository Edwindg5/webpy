from channels.generic.websocket import AsyncWebsocketConsumer
import json
from asgiref.sync import sync_to_async

from tutorial.models.profesor import Profesor
from .models import Carrera
from channels.layers import get_channel_layer
from channels.db import database_sync_to_async

class CarreraConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Unirse a un grupo para recibir actualizaciones
        await self.channel_layer.group_add(
            "carreras_updates",
            self.channel_name
        )
        await self.accept()
        
        # Envía los datos iniciales al cliente
        carreras = await self.get_carreras()
        await self.send(text_data=json.dumps(carreras))

    async def disconnect(self, close_code):
        # Abandonar el grupo al desconectar
        await self.channel_layer.group_discard(
            "carreras_updates",
            self.channel_name
        )

    async def receive(self, text_data):
        # Procesar mensajes recibidos del cliente si es necesario
        pass

    @database_sync_to_async
    def get_carreras(self):
        return list(Carrera.objects.values("id", "nombre"))

    async def carreras_update(self, event):
        # Enviar actualización al cliente cuando hay cambios
        carreras = await self.get_carreras()
        await self.send(text_data=json.dumps(carreras))
        
        
        
class ProfesorConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("profesores_updates", self.channel_name)
        await self.accept()
        await self.send_profesores()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("profesores_updates", self.channel_name)

    async def send_profesores(self):
        profesores = await self.get_profesores()
        await self.send(text_data=json.dumps({"profesores": profesores}))

    @database_sync_to_async
    def get_profesores(self):
        return list(Profesor.objects.values("id", "nombre", "apellido", "email", "telefono", "especialidad"))

    async def profesores_update(self, event):
        """ Enviar actualización en tiempo real a los clientes cuando se registre un nuevo profesor """
        await self.send(text_data=json.dumps({
            "tipo": "nuevo_profesor",
            "profesor": event["message"]
        }))
