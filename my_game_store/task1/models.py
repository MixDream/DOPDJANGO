from django.db import models

# Create your models here.
from django.db import models

class Buyer(models.Model):
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Game(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    age_limited = models.IntegerField()
    size = models.CharField(max_length=50)
    buyers = models.IntegerField(default=0)

    def __str__(self):
        return self.title

