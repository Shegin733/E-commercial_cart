

# Create your models here.
from django.db import models

from shops.models import product
from shops.models import *


class cartlist(models.Model):
    cart_id=models.CharField(max_length=150,unique=True)
    date_added=models.DateField(auto_now_add=True)
# Create your models here.
    def _str_(self):
       return self.cart_id
class items(models.Model):
    prodt=models.ForeignKey(product,on_delete=models.CASCADE)
    cart=models.ForeignKey(cartlist,on_delete=models.CASCADE)
    quan=models.IntegerField()
    active=models.BooleanField(default=True)
    def _str_(self):
       return self.prodt
    def total(self):
        return self.prodt.price*self.quan