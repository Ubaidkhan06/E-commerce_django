from django.urls import path
from . import views

urlpatterns = [
    path('',views.CartView, name='cart'),
    path('add_cart/<int:product_id>/',views.AddtoCartView, name='add_to_cart'),
    path('remove_cart/<int:product_id>/<int:cart_item_id>/',views.RemoveCartView, name='remove_from_cart'),
    path('remove_cart_item/<int:product_id>/<int:cart_item_id>/',views.RemoveCartItem, name='remove_item_from_cart'),
    path('checkout/', views.CheckoutView, name='checkout'),
]