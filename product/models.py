from django.db import models
from django.contrib.auth import get_user_model
from category.models import Category
from ckeditor.fields import RichTextField


User = get_user_model()


class Product(models.Model):
    STATUS_CHOICES = (
        ('in_stock', 'В наличии'),
        ('to_order', 'Под заказ')
    )
    title = models.CharField(max_length=150)
    # brand = models.CharField(max_length=100)
    # year = models.PositiveIntegerField()
    # mileage = models.PositiveIntegerField()
    # engine = models.CharField(max_length=100)
    # transmission = models.CharField(max_length=100)
    # drive_system = models.CharField(max_length=100)
    # model = models.CharField(max_length=100)
    description = RichTextField()
    category = models.ForeignKey(Category, related_name='products', on_delete=models.RESTRICT)
    image = models.ImageField(upload_to='images')
    price = models.DecimalField(max_digits=12, decimal_places=2)
    stock = models.CharField(choices=STATUS_CHOICES, max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    # def __str__(self):
    #     return f'{self.year} {self.brand} {self.model} {self.title}'


class ProductRequest(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f"Request for {self.product} by {self.name}"
