from django.urls import path
from . import views



urlpatterns = [
    path('', views.StoreView, name='store'),
    path('category/<slug:category_slug>/', views.StoreView, name='products_by_category'),
    path('category/<slug:category_slug>/<slug:product_slug>/', views.ProductDetailView, name='product_detail_view'),
    path('search/', views.SearchView, name='search'),
]