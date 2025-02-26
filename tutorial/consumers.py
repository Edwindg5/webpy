import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Carrera
from channels.db import database_sync_to_async


class MyConsumer(AsyncWebsocketConsumer):
    
   
    async def connect(self):
        await self.accept()
        carr = await self.getCarreras()
        await self.send(text_data=json.dumps({"message": "Connected"}))


    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data=None, bytes_data=None):
        if text_data:
            json = json.loads(text_data)
            json["message"]

@database_sync_to_async
def guardarCarrera(self, nombre, descripcion):
    carrera = Carrera.objects.create(nombre=nombre, descripcion=descripcion)
    carrera.save()
    return carrera
@database_sync_to_async
def getCarreras(self):
    return list(Carrera.objects.all().orderby('hombre'))



           
