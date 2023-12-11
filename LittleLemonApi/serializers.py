from rest_framework import serializers
from . models import MenueItem

class MenueItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenueItem
        fields = ['id','title','price','invetory']
        