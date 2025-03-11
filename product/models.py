from django.db import models
import uuid
from django.core.validators import MaxValueValidator

# Create your models here.

class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=40)
    description = models.TextField()
    price = models.IntegerField(validators=[MaxValueValidator(100)])


    class Meta:
        db_table = "products" 
        ordering = ['price']  # Default order by price (ascending)
        verbose_name = "Product Item"  # Custom model name in admin panel
        verbose_name_plural = "Product Items"  # Plural name in admin
        constraints = [
            models.CheckConstraint(check=models.Q(price__gte=0), name="price_non_negative")  # Ensures price is >= 0
        ]
    
    def __str__(self):
        return f"{self.title} - ${self.price}"

