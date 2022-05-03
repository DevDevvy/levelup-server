from django.db import models

from levelupapi.models.gamer import Gamer

class Event(models.Model):
    game = models.ForeignKey('game', on_delete=models.CASCADE)
    description = models.CharField(max_length=200, default=None)
    game_date = models.CharField(max_length=10, default=None)
    time = models.CharField(max_length=10, default=None)
    organizer = models.ForeignKey("gamer", on_delete=models.CASCADE)
    attendees = models.ManyToManyField(Gamer, related_name="gamers")
    
    @property
    def joined(self):
        return self.__joined
    
    @joined.setter
    def joined(self, value):
        self.__joined = value