from django.urls import re_path
from django.urls import include
from rest_framework.routers import DefaultRouter
from product import views

app_name = "product"

router = DefaultRouter()

router.register(r'product', views.ProductViewset)

urlpatterns = [
    re_path(r'^', include(router.urls)),
    re_path(r'order_price/(?P<order>[-\w]+)/$',views.ProductAPIView.list_price),
    re_path(r'order_popularity/(?P<order>[-\w]+)/$',views.ProductAPIView.list_popularity),
    re_path(r'order_name/(?P<order>[-\w]+)/$',views.ProductAPIView.list_name),

]
