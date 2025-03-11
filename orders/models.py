from django.db import models

# Create your models here.

class Order(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=3,decimal_places=2)

    class Meta:
        db_table = "orders"
        ordering = ["price"]

    def __str__(self):
        return f"{self.title} - ${self.price}"