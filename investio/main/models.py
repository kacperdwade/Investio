from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Investment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="investment", null=True)
    name = models.CharField(max_length=50)
    img = models.CharField(max_length=200)
    location = models.CharField(max_length=50)
    about = models.CharField(max_length=200)
    price = models.FloatField()
    ror = models.IntegerField()
    tor = models.IntegerField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


