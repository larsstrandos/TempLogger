from django.db import models

# Create your models here.
class temp(models.Model):
    reader_id = models.IntegerField()
    time = models.DateTimeField(auto_now=False, auto_now_add=True)
    temp = models.DecimalField( max_digits=5, decimal_places=2)