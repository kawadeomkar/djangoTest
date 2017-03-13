from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class ParkingSpot(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=25, default="")
    zipcode = models.CharField(max_length=5, default="")
    street = models.CharField(max_length=50, default="")
    city = models.CharField(max_length=15, default="")
    state = models.CharField(max_length=2, default="")
    price = models.IntegerField(default=0)
    picture = models.FileField(null=True, blank=True)
    posttime = models.DateTimeField(default="YYYY-MM-DD")
    description = models.TextField(max_length=1000, default="")

    def get_absolute_url(self):
        return reverse('')

    def __str__(self):
        return self.owner, self.title
