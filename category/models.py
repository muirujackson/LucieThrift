from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(max_length=255, blank=True, null=True)
    cat_image = models.ImageField(upload_to='photos/categories', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        
    def __str__(self):
        return self.category_name