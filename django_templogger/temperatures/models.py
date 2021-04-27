from django.db import models

class Temp(models.Model):
    sensor_id = models.IntegerField()
    temp = models.DecimalField( max_digits=5, decimal_places=2)
    created_date = models.DateTimeField(auto_now=False, auto_now_add=True)

#    def currentTemp(rid):
        