from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import GroceryItem
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import GroceryItemSerializer
def members(request):
    return render(request,"base.html")

   




class GroceryItemCreateAPIView(generics.CreateAPIView):
    queryset = GroceryItem.objects.all()
    serializer_class = GroceryItemSerializer




class listgroceries(generics.ListAPIView):
    serializer_class = GroceryItemSerializer

    def get_queryset(self):
        queryset = GroceryItem.objects.all()

        # Get parameters from the query string
        category = self.request.query_params.get('category', None)
        is_available = self.request.query_params.get('is_available', None)

        # Apply filters only if provided
        if category:
            queryset = queryset.filter(category=category)

        if is_available is not None:
            is_available = is_available.lower() == 'true'
            queryset = queryset.filter(is_available=is_available)

        return queryset
    


class DeleteGroceryItem(generics.DestroyAPIView):
    queryset = GroceryItem.objects.all()
    serializer_class = GroceryItemSerializer

class UpdateGroceryItem(generics.UpdateAPIView):
    queryset = GroceryItem.objects.all()
    serializer_class = GroceryItemSerializer

