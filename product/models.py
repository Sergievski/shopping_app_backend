from django.db import models
from django.db import models
from django.contrib.auth.models import User


def upload_path(instance, filename):
    return '/'.join(['images', str(instance.name), filename])


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    image = models.ImageField(upload_to=upload_path,  null=True, blank=True, default='/images/placeholder.png')
    archived = models.BooleanField ( default = False)
                            

class Cart(models.Model):
    # name = models.CharField(max_length=200, default = "Name")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product") # nested serialiser 
    quantity = models.IntegerField(default=1, null=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    
    

    