from django.urls import path
from . import views



urlpatterns = [
     path('products/', views.products ),
     path('products/<int:pk>', views.single_product),
     path('cart-items/<int:pk>', views.single_item),
     path('cart-items/', views.items)
    
] 



