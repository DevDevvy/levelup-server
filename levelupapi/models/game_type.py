from django.db import models

class Game_type(models.Model):
    type = models.CharField(max_length=20)