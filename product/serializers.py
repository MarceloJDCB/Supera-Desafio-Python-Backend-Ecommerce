from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField
from django.contrib.auth.models import User
from .models import Product,ProductOrder, Order

class ProductSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=150,
                                allow_blank=False,
                                allow_null=False,
                                required=True)
    
    price = serializers.DecimalField(max_digits=6,
                                    decimal_places=2,
                                    allow_null=False,
                                    required=True)
    score = serializers.IntegerField(
                                allow_null=False,
                                required=True)
    
    image = Base64ImageField(allow_empty_file=True, 
                             max_length=None, 
                             use_url=False, 
                             #write_only=True, 
                             required=False)
    class Meta:
        model = Product
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(queryset=User.objects.all(),
                                          slug_field='id')
    
    value = serializers.DecimalField(max_digits=6,
                                    decimal_places=2,
                                    allow_null=False,
                                    required=True)
    freight = serializers.IntegerField(
                                allow_null=False,
                                required=True)
    

    class Meta:
        model = Order
        fields = '__all__'
        
class ProductOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOrder
        fields = '__all__'