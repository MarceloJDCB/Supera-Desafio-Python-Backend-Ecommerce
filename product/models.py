from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    popularity = models.IntegerField()
    image = models.FileField(upload_to='static/imgs')
    
