from django.db import models
from categories.models import Category

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to='products/images/', null=True, blank=True)
    price = models.FloatField()
    instock = models.IntegerField()
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'

    def get_image_url(self):
        return f'/media/{self.image}'