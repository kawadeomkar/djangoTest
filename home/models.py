from django.db import models


class ParkingSpot(models.Model):
    owner = models.CharField(max_length=25)
    title = models.CharField(max_length=25)
    zip = models.CharField(max_length=5)
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=15)
    state = models.CharField(max_length=2)
    price = models.IntegerField()
    picture = models.FileField(null=True)

    def __str__(self):
        return self.owner
