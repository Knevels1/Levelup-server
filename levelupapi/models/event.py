from django.db import models
from .game import Game
from .gamer import Gamer


class Event(models.Model):

    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    location = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()
    scheduler = models.ForeignKey(Gamer, on_delete=models.CASCADE)