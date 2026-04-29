from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200,unique=True)
    slug = models.SlugField(max_length=50, unique=True)



    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True,related_name='products')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveBigIntegerField(default=0)
    image = models.ImageField(upload_to='products/', null=True)

    def __str__(self):
        return self.name
    








