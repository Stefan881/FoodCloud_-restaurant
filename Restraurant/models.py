from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    price = models.CharField(max_length=100, blank=False, null=False)
    description = models.CharField(max_length=100, blank=False, null=False)
    image = models.ImageField(blank=False,null=True,upload_to='assets/images')


    def __str__(self):
        return self.name

