from django.contrib import admin
from .models import Category

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}
    list_display = ('category_name', 'slug', 'description', 'cat_image', 'created_at', 'updated_at')
    list_filter = ('category_name', 'created_at')
    search_fields = ('category_name', 'description')
    list_per_page = 20
    

admin.site.register(Category, CategoryAdmin)