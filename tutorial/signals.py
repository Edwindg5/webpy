from django.db.models.signals import post_save
from django.dispatch import receiver
from tutorial.models.profesor import Profesor
from channels.layers import get_channel_layer
import json
from asgiref.sync import async_to_sync

@receiver(post_save, sender=Profesor)
def notify_profesor_created(sender, instance, **kwargs):
    channel_layer = get_channel_layer()
    data = {
        "id": instance.id,
        "nombre": instance.nombre,
        "apellido": instance.apellido,
        "email": instance.email,
        "telefono": instance.telefono,
        "especialidad": instance.especialidad,
    }
    async_to_sync(channel_layer.group_send)(
        "profesores_updates",
        {"type": "profesores_update", "data": json.dumps(data)},
    )
