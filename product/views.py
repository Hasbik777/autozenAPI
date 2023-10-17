from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions, response, generics
from rest_framework.decorators import action
from .models import Product, ProductRequest
from .serializers import ProductRequestSerializer
from . import serializers
from .permissions import IsAuthor
# Create your views here.


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.ProductListSerializer
        return serializers.ProductSerializer

    def get_permissions(self):
        if self.action in ('update', 'partial_update', 'destroy'):
            return [permissions.IsAuthenticated(), IsAuthor()]
        return [permissions.IsAuthenticatedOrReadOnly()]

    @action(['DELETE'], detail=True)
    def review_delete(self, request, pk):
        product = self.get_object() # Product.objects.get(id=pk)
        user = request.user
        if not product.reviews.filter(owner=user).exists():
            return response.Response('You did not reviewed this product!',
                                     status=400)
        review = product.reviews.get(owner=user)
        review.delete()
        return response.Response('Successfully deleted', status=204)


class ProductRequestListCreateView(generics.ListCreateAPIView):
    queryset = ProductRequest.objects.all()
    serializer_class = ProductRequestSerializer


class ProductRequestDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductRequest.objects.all()
    serializer_class = ProductRequestSerializer
