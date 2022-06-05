from django import views
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from .serializers import ProductSerializer,OrderSerializer, ProductOrderSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.authentication import SessionAuthentication,BasicAuthentication
from .productfn import ProductFn
from .models import Product,Order, ProductOrder

class OrderViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
    def create(self,request):
        params = request.data
        author = params['author']
        value = params['itemsPrice']
        freight = params['freightPrice']
        totalprice = params['totalPrice']
        products = params['orderItems']
        
        data = {"author":author,
                "value":value,
                "freight":freight,
                "totalprice":totalprice,
                "products":[]}
        for product in products:
            product_data = {"product":product['product'],"qty":product['qty']}
            serializer = ProductOrderSerializer(data=product_data)
            serializer.is_valid(raise_exception=True)
            obj = serializer.save()
            data['products'].append(obj.id)
        
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        
                
        
        return Response(data=serializer.data,status=status.HTTP_201_CREATED)
    
    def list_my_orders(self,request,userid):
        orders = Order.objects.filter(author=userid)
        
        serializer = OrderSerializer(data=orders,many=True)
        serializer.is_valid(raise_exception=False)
        return Response(data=serializer.data,status=status.HTTP_200_OK)

class ProductOrderViewset(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    authentication_classes = ()
    
    
    queryset = ProductOrder.objects.all()
    serializer_class = ProductOrderSerializer
    

class ProductViewset(viewsets.ModelViewSet):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    def list(self,request):
        product_list = Product.objects.all()
        products = []
        for product in product_list:
            payload = {
                "id":product.id,
                "name":product.name,
                "price":product.price,
                "score":product.score,
                "image":product.base64
            }
            products.append(payload)
        return Response(data=products)    
    
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
        return ProductFn.list_product(order,'price')
       
    @api_view(('GET',))
    def list_score(request,order):
        return ProductFn.list_product(order,'score')

    @api_view(('GET',))
    def list_name(request,order):
        return ProductFn.list_product(order,'name')
       