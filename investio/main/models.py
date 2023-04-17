from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.

class Investment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="investment", null=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    about = models.CharField(max_length=200)
    price = models.FloatField()
    ror = models.IntegerField()
    tor = models.IntegerField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("main:investment-detail-view", kwargs={"id_": self.id})

    #
    def save(self, *args, **kwargs):
        self.location = self.location.lower()
        return super(Investment, self).save(*args, **kwargs)


def make_file_path(instance, filename):
    id = instance.investment.id
    path = f'images/{id}/{filename}'
    return path
class Image(models.Model):
    investment = models.ForeignKey(Investment, on_delete=models.CASCADE, related_name='image', null=True)
    img = models.FileField(null=True, blank=True, upload_to=make_file_path)


