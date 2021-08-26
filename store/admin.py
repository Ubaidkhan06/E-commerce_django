from django.contrib import admin
from .models import Product
# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    '''Admin View for Product'''

    list_display = ('product_name', 'price', 'stock', 'category', 'date_created', 'date_modified', 'is_available')
    prepopulated_fields = {'slug':('product_name',)}