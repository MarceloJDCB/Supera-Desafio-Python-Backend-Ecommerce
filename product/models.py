from django.db import models
from django.contrib.auth.models import User
import base64

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    popularity = models.IntegerField()
    image = models.FileField(upload_to='static/imgs')
    
    @property
    def base64(self):
        path = str(self.image)
        try:
            with open(path, 'rb') as f:
                content = f.read()
            img = "data:image/png;base64," + (base64.b64encode(content)).decode()
        except:
            img = ("Imagem não encontrada no nosso banco de dados...")
        return img

class Order(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=6,decimal_places=2)
    freight = models.DecimalField(max_digits=5,decimal_places=2)
    products = models.ManyToManyField(Product)