from django.urls import path
from .views import ProductRequestListCreateView, ProductRequestDetailView

urlpatterns = [
    path('product-requests/', ProductRequestListCreateView.as_view()),
    path('product-requests/<int:pk>/', ProductRequestDetailView.as_view())
]
