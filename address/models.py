from django.db import models


class Address(models.Model):
    address = models.CharField(max_length=255)
    lat = models.FloatField()
    lon = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
