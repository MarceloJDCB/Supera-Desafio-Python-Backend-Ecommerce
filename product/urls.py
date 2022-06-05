from django.urls import re_path
from django.urls import include
from rest_framework.routers import DefaultRouter
from product import views

app_name = "product"

router = DefaultRouter()

router.register(r'product', views.ProductViewset)
router.register(r'order', views.OrderViewset)
router.register(r'productorder', views.ProductOrderViewset)


urlpatterns = [
    re_path(r'^', include(router.urls)),
    re_path(r'order_price/(?P<order>[-\w]+)/$',views.ProductAPIView.list_price),
    re_path(r'order_score/(?P<order>[-\w]+)/$',views.ProductAPIView.list_score),
    re_path(r'order_name/(?P<order>[-\w]+)/$',views.ProductAPIView.list_name),
    re_path(r'list-my-orders/(?P<userid>[-\w]+)/$',views.OrderViewset.as_view({"get": "list_my_orders"}))
    

]
