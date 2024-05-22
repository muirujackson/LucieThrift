from django.contrib import admin
from .models import Product, Category

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'category', 'created_at', 'updated_at')
    list_filter = ('category', 'created_at')
    list_editable = ('price', 'stock', 'category')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Product, ProductAdmin)