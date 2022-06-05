from django.urls import re_path
from django.urls import include
from rest_framework.routers import DefaultRouter
from UserManagement import views

app_name = "user"

router = DefaultRouter()

urlpatterns = [
    re_path(r'^', include(router.urls)),
    re_path(r'register/',views.RegisterAPIView.as_view()),
    re_path(r'login/',views.LoginAPIView.as_view()),
    

]
