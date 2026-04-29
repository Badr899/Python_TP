from django.urls import path
from . import views
from .views import ProductListView, ProductDetailView

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
]