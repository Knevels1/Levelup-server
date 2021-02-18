from django.db import models
from .event import Event
from .gamer import Gamer


class EventGamer(models.Model):

    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    gamer_id = models.ForeignKey(Gamer, on_delete=models.CASCADE)