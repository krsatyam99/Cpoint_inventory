from django.contrib import admin
from inventory.models import GroceryItem
# Register your models here.
class Inventory_admin(admin.ModelAdmin):
    list_display=('id','name','quantity','price','created_at','is_available','category')
    ordering = ('created_at',)
admin.site.register(GroceryItem,Inventory_admin)