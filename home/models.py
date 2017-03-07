from django.db import models


class ParkingSpot(models.Model):
    owner = models.CharField(max_length=25, default="")
    title = models.CharField(max_length=25, default="")
    zipcode = models.CharField(max_length=5, default="")
    street = models.CharField(max_length=50, default="")
    city = models.CharField(max_length=15, default="")
    state = models.CharField(max_length=2, default="")
    price = models.IntegerField(default=0)
    picture = models.FileField(null=True)

    def __str__(self):
        return self.title
