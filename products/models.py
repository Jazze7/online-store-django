from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=255)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    image = models.ImageField(upload_to='product_images/')
    quantity=models.PositiveIntegerField()
    is_deleted=models.BooleanField(default=False)

    class Meta:
        db_table = 'product'
        
    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.product.price * self.quantity