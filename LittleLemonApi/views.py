from django.shortcuts import render
from . models import MenueItem
from .serializers import MenueItemSerializer
from rest_framework import generics

class MenueItemView(generics.ListCreateAPIView):
    queryset = MenueItem.objects.all()
    serializer_class = MenueItemSerializer
    
class SingleMenueItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenueItem.objects.all()
    serializer_class = MenueItemSerializer
    
