from django.db import models

class Event(models.Model):
    game = models.ForeignKey('game', on_delete=models.CASCADE)
    description = models.CharField(max_length=200, default=None)
    game_date = models.CharField(max_length=10, default=None)
    time = models.CharField(max_length=10, default=None)
    organizer = models.ForeignKey("gamer", on_delete=models.CASCADE)