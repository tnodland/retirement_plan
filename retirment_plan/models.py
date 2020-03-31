from django.db import models

class Bug(models.Model):
    name = models.CharField(null=False, max_length=255)
    price = models.IntegerField(default=0)
    location = models.CharField(null=False, max_length=255)
    time = models.TimeField()
    hemisphere = models.CharField(null=False, max_length=255)
