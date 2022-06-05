from product.models import Product
from rest_framework.response import Response

class ProductFn:
    
    def list_product(order,attribute):
        if order == "minor":
            product_list = Product.objects.order_by(attribute)
        else:
            product_list = Product.objects.order_by(f'-{attribute}')
            
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