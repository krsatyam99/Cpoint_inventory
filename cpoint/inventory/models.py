from django.db import models




class GroceryItem(models.Model):
    CATEGORY_CHOICES = {
        'fruits': 'Fruits',
        'vegetables': 'Vegetables',
        'dairy': 'Dairy',
        'meat': 'Meat',
        'snacks': 'Snacks',
        'beverages': 'Beverages',
        'other': 'Other',
    }

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_available = models.BooleanField(default=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES.items())
    image = models.ImageField(upload_to='static/grocery_image/', blank=True, null=True)




    def __str__(self):
        return self.name