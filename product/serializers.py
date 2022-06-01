from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=150,
                                allow_blank=False,
                                allow_null=False,
                                required=True)
    
    price = serializers.DecimalField(max_digits=6,
                                    decimal_places=2,
                                    allow_null=False,
                                    required=True)
    popularity = serializers.IntegerField(
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
