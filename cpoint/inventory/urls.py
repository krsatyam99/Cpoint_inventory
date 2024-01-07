from django.urls import path
from . import views
from inventory.views import GroceryItemCreateAPIView,listgroceries,DeleteGroceryItem,UpdateGroceryItem


urlpatterns = [
    path('members/', views.members, name='members'),

    path('grocery/', GroceryItemCreateAPIView.as_view(), name='grocery-item-create'),
    path('grocery_list/', listgroceries.as_view(), name='grocery-item-list'),
    path('grocery/<int:pk>/delete/', DeleteGroceryItem.as_view(), name='delete-grocery-item'),
    path('grocery/<int:pk>/update/', UpdateGroceryItem.as_view(), name='update-grocery-item'),





]