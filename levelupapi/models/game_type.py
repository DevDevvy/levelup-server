from cProfile import label
from django.db import models

class Game_type(models.Model):
    label = models.CharField(max_length=20)