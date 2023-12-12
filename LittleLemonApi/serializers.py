from rest_framework import serializers
from . models import MenueItem
from decimal import Decimal

class MenueItemSerializer(serializers.ModelSerializer):
    stock = serializers.IntegerField(source= 'invetory')
    discounted_price_ = serializers.SerializerMethodField(method_name='discounted_price')
    class Meta:
        model = MenueItem
        fields = ['id','title','price','stock','discounted_price_']
        
    def discounted_price(self,product:MenueItem):
        return product.price -((product.price*10)/100)
        