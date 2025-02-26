import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Carrera


class MyConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        await self.accept()
        await self.enviar_carreras()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data=None, bytes_data=None):
        if text_data:
            data = json.loads(text_data)
            print(data["message"])
            if data.get("action") == "get_carreras":
                await self.enviar_carreras()

    @database_sync_to_async
    def guardarCarrera(self, nombre, descripcion):
        carrera = Carrera.objects.create(nombre=nombre, descripcion=descripcion)
        carrera.save()
        return carrera

    @database_sync_to_async
    def getCarreras(self):
        return list(Carrera.objects.all().order_by('nombre'))

    async def enviar_carreras(self):
        carr = await self.getCarreras()
        data = [{'nombre': c.nombre, 'descripcion': c.descripcion} for c in carr]
        await self.send(text_data=json.dumps({"message": data}))
