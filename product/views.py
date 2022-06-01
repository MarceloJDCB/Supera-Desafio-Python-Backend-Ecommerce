from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from .serializers import ProductSerializer
from .models import Product

class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def retrieve(self, request, pk=None):
        product = get_object_or_404(self.queryset, pk=pk)
        print(type(product),product)
        serializer = self.serializer_class(product)
        payload = serializer.data
        payload['img'] = product.base64
        return Response(data=payload)
 
class ProductAPIView(APIView):
    
    @api_view(('GET',))
    def list_price(request,order):
        if order == "minor":
            product_list = Product.objects.order_by('price')
        else:
            product_list = Product.objects.order_by('-price')
        products = []
        for product in product_list:
            payload = {
                "name":product.name,
                "price":product.price,
                "popularity":product.popularity,
                "image":product.base64
            }
            products.append(payload)
        return Response(data=products)
    
    @api_view(('GET',))
    def list_popularity(request,order):
        if order == "minor":
            product_list = Product.objects.order_by('popularity')
        else:
            product_list = Product.objects.order_by('-popularity')
        products = []
        for product in product_list:
            payload = {
                "name":product.name,
                "price":product.price,
                "popularity":product.popularity,
                "image":product.base64
            }
            products.append(payload)
        return Response(data=products)
    
    @api_view(('GET',))
    def list_name(request,order):
        if order == "minor":
            product_list = Product.objects.order_by('name')
        else:
            product_list = Product.objects.order_by('-name')
        products = []
        for product in product_list:
            payload = {
                "name":product.name,
                "price":product.price,
                "popularity":product.popularity,
                "image":product.base64
            }
            products.append(payload)
        return Response(data=products)