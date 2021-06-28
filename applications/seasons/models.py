from django.db import models

# Create your models here.

class Order(models.Model):
    
    
    
    ord_dt = models.DateField()
    qt_ordd = models.IntegerField()
    
    