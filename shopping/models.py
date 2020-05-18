from django.db import models


# so what do i need?
# i need a cart, and items to put in it
# so a cart is something that is associated to a User, and items are associated to a cart
# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length = 200)
    price = models.IntegerField()
    def __str__(self):
        return f"{self.name} : {self.price}"

class ItemInCart(models.Model):
    name = models.CharField(max_length = 200)
    price = models.IntegerField()
    frequency = models.IntegerField()
    def __str__(self):
        return f"{self.name} : {self.price} : {self.frequency}"

class Cart(models.Model):
    user = models.CharField(max_length = 64)
    items  = models.ManyToManyField(ItemInCart, blank = True,related_name = 'bag')




