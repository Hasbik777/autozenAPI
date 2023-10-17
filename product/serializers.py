from rest_framework import serializers
from .models import Product, ProductRequest


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('title', 'price', 'image', 'stock')


class ProductRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductRequest
        fields = '__all__'
