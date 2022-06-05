from .serializers import RegistrationSerializer, LoginSerializer, UserSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib.auth import login
from rest_framework.permissions import AllowAny
from rest_framework import status,viewsets



class RegisterAPIView(APIView):

    def post(self, request):
        params = request.data
        serializer = RegistrationSerializer(data=params)
        
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"user": serializer.data}, status=status.HTTP_201_CREATED)
    
class LoginAPIView(APIView):
    def post(self, request):
        print(request.data)
        #print(request.data['username'])
        serializer = LoginSerializer(data=request.data)
        
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        login(request, user)
        token, create = Token.objects.get_or_create(user=user)
        user = User.objects.get(username=user)
        user_serializer = UserSerializer(user)
        return Response({
            "token": token.key,
            "user": user_serializer.data
        }, status=status.HTTP_200_OK)