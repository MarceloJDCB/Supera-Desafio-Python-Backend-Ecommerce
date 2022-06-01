from django.urls import re_path
from django.urls import include
from rest_framework.routers import DefaultRouter
from product import views

app_name = "product"

router = DefaultRouter()

router.register(r'product', views.ProductViewset)

urlpatterns = [
    re_path(r'^', include(router.urls)),
]
