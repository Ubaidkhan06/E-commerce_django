from ast import AugLoad
from django.db import models
from category.models import Category
from django.urls import reverse
# Create your models here.

class Product(models.Model):

    product_name    = models.CharField(max_length=50, unique=True)
    slug            = models.SlugField(max_length=255, unique=True)
    description     = models.CharField(max_length=255, unique=True)
    price           = models.FloatField()
    is_available    = models.BooleanField(default=True)
    stock           = models.IntegerField()
    images          = models.ImageField(upload_to='photos/products')
    category        = models.ForeignKey(Category, on_delete=models.CASCADE)
    date_created    = models.DateTimeField(auto_now_add=True)
    date_modified   = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('product_detail_view', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.product_name

class VariationManager(models.Manager):
    def colours(self):
        return super(VariationManager, self).filter(variation_category='colour', is_active=True)

    def sizes(self):
        return super(VariationManager, self).filter(variation_category='size', is_active=True)

variation_category_choice = (
    ('colour', 'colour'), ('size', 'size')
)

class Variation(models.Model):
    product             = models.ForeignKey(Product, on_delete=models.CASCADE)
    variation_category  = models.CharField(max_length=100, choices=variation_category_choice)
    variation_value     = models.CharField(max_length=100)
    is_active           = models.BooleanField(default=True)
    date_created        = models.DateTimeField(auto_now_add=True)

    objects = VariationManager()

    def __str__(self):
        return (self.variation_value)