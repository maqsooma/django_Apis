from django.db import models

# Create your models here.
class MenueItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6,decimal_places=3)
    invetory = models.SmallIntegerField()
    
    
