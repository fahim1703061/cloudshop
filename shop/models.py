from django.db import models
from product.models import Customer

# Create your models here.


class Shop(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    shopurl = models.CharField(max_length=200, null=True, unique=True)
    image = models.ImageField(
        upload_to='shop/images', null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    phone = models.CharField(
        max_length=200, default=0, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    state = models.CharField(max_length=200, null=True, blank=True)
    zipcode = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
