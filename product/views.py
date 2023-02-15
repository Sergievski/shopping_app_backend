from django.shortcuts import redirect, render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from product.models import Product, CartItem, Cart
from product.serializers import ProductSerializer, CartSerializer, CartItemSerializer
from django.db.models import Q


###### PRODUCTS  ###########################################

@api_view(['GET', 'POST'])
def products(request):
   
    if request.method == 'GET': # show all/searched products 
        q = request.GET.get('query') if request.GET.get('query') != None else ''
        products = Product.objects.filter(
        Q(archived = False) & Q(name__icontains=q) 
        )
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':  # add product
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def single_product(request, pk):
    try: 
        product = Product.objects.get(id=pk) 
        
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET' : # get single product 
        serializer = ProductSerializer(product, many=False)
        return Response(serializer.data)
    if request.method == 'DELETE': # delete product (send to archive ) 
        product.archived = True
        product.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
    if request.method == 'PUT' :  #update product
        serializer = ProductSerializer(instance=product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    ########################################################################################################
    
    ##########  CART  ###########################################
    
    
@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def items(request):
    # user = request.user
    
    if request.method == 'GET': # show all user items 
        items = CartItem.objects.all()
        serializer = CartItemSerializer (items, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST': # add item ( add product to cart)
        try:
            productId = request.data.get('productId')
            product = Product.objects.get(id=productId)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
        cart, created = Cart.objects.get_or_create()
        quantity = request.data.get('quantity')
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if not created:
            cart_item.quantity += int(quantity)    
        else:
            cart_item.quantity = int(quantity)           
        cart_item.save()
        return Response(status=status.HTTP_201_CREATED)
            
    
@api_view(['PUT', 'DELETE', 'GET'])
def single_item(request, pk) :
    
    try: 
        
        cart_item = CartItem.objects.get(id=pk) 
        
    except CartItem.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    
    if request.method == 'GET' :   # get single item (product in cart)
        serializer = CartItemSerializer(cart_item, many=False)
        return Response(serializer.data)
    
    
    if request.method == 'DELETE': # delete item
       cart_item.delete()
       return Response(status=status.HTTP_204_NO_CONTENT)
           
           
    if request.method == 'PUT' :  # update item (quantity) in cart 
        quantity = request.data.get('quantity')
        cart_item.quantity = int(quantity)
        cart_item.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
        

       
       
    
