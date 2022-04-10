from django.urls import path
from django.views import View

from .views import ProductListView, ProductDetailView
urlpatterns = [
    path('', ProductListView.as_view()),
    path('/<int:product_id>', ProductDetailView.as_view())
]