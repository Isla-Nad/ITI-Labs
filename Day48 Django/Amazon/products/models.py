from django.db import models
from django.shortcuts import reverse
from categories.models import Category


class Product(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to='products/images/', max_length=200)
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

    def get_show_url(self):
        url = reverse('products.profile', args=[self.id])
        return url
