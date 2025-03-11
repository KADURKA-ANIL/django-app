from django.urls import path
from .views import ProductView

urlpatterns = [
    path('product/', ProductView.as_view(), name='product_api'),  # Handles GET, POST, PUT, DELETE
]
