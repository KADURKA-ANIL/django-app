from django.db import models
import uuid
# Create your models here.

class Student(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=45,null=False,blank=False)
    email = models.EmailField(max_length=80,null=False,blank=False)
    age = models.IntegerField(null=False,blank=False)
    scholarship = models.BooleanField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

    class Meta:
        db_table = "students"  # Custom table name
        ordering = ["-created_at"]  # Default ordering by latest created
    
    def __str__(self):
        return self.name