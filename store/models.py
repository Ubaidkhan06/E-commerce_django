from django.db import models
from category.models import Category
from django.urls import reverse
# Create your models here.

class Product(models.Model):

    product_name   = models.CharField(max_length=50, unique=True)
    slug            = models.SlugField(max_length=255, unique=True)
    description     = models.CharField(max_length=255, unique=True)
    price           = models.FloatField()
    is_available    = models.BooleanField(default=True)
    stock           = models.IntegerField()
    images          = models.ImageField(upload_to='photos/products')
    category        = models.ForeignKey(Category, on_delete=models.CASCADE)
    date_created    = models.DateTimeField(auto_now_add=True)
    date_modified    = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('product_detail_view', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.product_name