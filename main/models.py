import uuid
from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('jersey', 'Jersey'),
        ('shoes', 'Shoes'),
        ('shorts', 'Shorts'),
        ('accessories', 'Accessories'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='jersey')
    product_views = models.PositiveIntegerField(default=0)
    is_featured = models.BooleanField(default=False) 

    def __str__(self):
        return self.name
        
    def increment_views(self):
        self.product_views += 1
        self.save()