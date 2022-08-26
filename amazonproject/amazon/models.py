from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.TextField()
    image = models.ImageField(upload_to='gallery')
    desc = models.TextField()
    mrp = models.FloatField()
    price = models.FloatField()

    def __str__(self):
        return self.name
