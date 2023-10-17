from django.urls import path
from .views import RequestDetailView, RequestListCreateView

urlpatterns = [
    path('requests/', RequestListCreateView.as_view()),
    path('requests/<int:pk>/', RequestDetailView.as_view()),
]
