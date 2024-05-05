from django.db import models
from django.contrib.postgres.fields import ArrayField

def default_array():
    return []

class Character(models.Model):
    name = models.CharField(max_length=100, default='empty')
    character_class = models.CharField(max_length=100, default='empty')
    strength = models.IntegerField(default=0)
    dexterity = models.IntegerField(default=0)
    constitution = models.IntegerField(default=0)
    intelligence = models.IntegerField(default=0)
    wisdom = models.IntegerField(default=0)
    charisma = models.IntegerField(default=0)
    stress = models.IntegerField(default=0)
    mental_scars = models.CharField(max_length=100, default='empty')
    valors = models.CharField(max_length=100, default='empty')
    description = models.CharField(max_length=300, default='empty')
    armour_class = models.IntegerField(default=0)
    health_points = models.IntegerField(default=0)
    image = models.ImageField(upload_to="media/characterPhoto")

    def __str__(self):
        return self.name

