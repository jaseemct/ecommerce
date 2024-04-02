from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=30)

    def __str__(self):
        return self.category_name
    
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True)
    product_name = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=255)  
    price = models.IntegerField() 
    image=models.ImageField(upload_to="image/", null=True) 

    def __str__(self):
        return self.product_name
    
class Signup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    address = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=20)
    image= models.ImageField(blank=True, upload_to='images/',null=True)
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    quantity=models.PositiveIntegerField(default=1)
    
    def total_price(self):
        return self.quantity * self.product.price