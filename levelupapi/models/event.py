from django.db import models


class Event(models.Model):

        scheduler = models.ForeignKey("Gamer", on_delete=models.CASCADE)
        game = models.ForeignKey("Game", on_delete=models.CASCADE)
        scheduled_time = models.DateTimeField(auto_now=False, auto_now_add=False)
        location = models.CharField(max_length=50)