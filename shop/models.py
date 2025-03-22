from django.db import models
from django.core.exceptions import ValidationError
 

# Create your models here.

def validate_image_size(value):
    # 1MB = 1024 * 1024 bytes
    max_size = 1024 * 1024
    if value.size > max_size: raise ValidationError(f'The image size should not exceed {max_size} bytes (1MB)')


class Product(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True) # Optional field
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    category = models.CharField(max_length=100)
    image = models.ImageField(default="Product.jpg", upload_to="product_images/", validators = [validate_image_size], blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name
