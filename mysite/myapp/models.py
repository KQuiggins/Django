from django.db import models

class Product(models.Model):
    def __str__(self) -> str:
        return self.name
    
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    desc = models.CharField(max_length=200)
    image = models.ImageField(blank=True, upload_to='images')

    
