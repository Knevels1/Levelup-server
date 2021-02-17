from django.db import models
from .gamer import Gamer
from .gametype import GameType



class Games(models.Model):
    
    gamer = models.ForeignKey(Gamer, on_delete=models.CASCADE)
    gametype = models.ForeignKey(GameType, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.CharField( max_length=255)
    number_of_players = models.IntegerField()