from rest_framework import serializers
from product.models import Product, Cart, CartItem

 
        
class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'created', 'updated', 'image')
        
    
class CartSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Cart
        fields = "__all__"
        
   
class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=False, read_only=True) #nested serializer
    class Meta:
        model = CartItem
        fields = "__all__"
        