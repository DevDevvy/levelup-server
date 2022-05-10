from django.db import models


class Event(models.Model):
    game = models.ForeignKey('game', related_name='events', on_delete=models.CASCADE)
    description = models.CharField(max_length=200, default=None)
    game_date = models.DateField(auto_now=False, auto_now_add=False)
    time = models.CharField(max_length=10, default=None)
    organizer = models.ForeignKey("gamer", on_delete=models.CASCADE)
    attendees = models.ManyToManyField("Gamer", through="event_gamer", related_name="events") 
    
    @property
    def joined(self):
        return self.__joined
    
    @joined.setter
    def joined(self, value):
        self.__joined = value