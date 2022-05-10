from django.db import models

# Create your models here.
# import datetime
class CSV(models.Model):
    timestamp = models.TimeField()
    load_value = models.FloatField(null=True)
    date = models.DateField()

    def __str__(self):
        return "yes"