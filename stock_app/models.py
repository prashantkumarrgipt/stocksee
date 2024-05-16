from django.contrib.auth.models import User
from django.db import models

class Stock(models.Model):
    symbol = models.CharField(max_length=10)

class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stocks = models.ManyToManyField(Stock)
