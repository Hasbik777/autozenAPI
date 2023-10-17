from django.shortcuts import render
from rest_framework import generics
from .models import Request
from account.serializers import RequestSerializer


# Create your views here.
class RequestListCreateView(generics.ListCreateAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer


class RequestDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
