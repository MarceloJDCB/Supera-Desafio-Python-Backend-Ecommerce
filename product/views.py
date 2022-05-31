from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render

class IndexTestView(APIView):
    @api_view(('GET',))
    def index(request):
        return Response(data={"hello":"word"},status=status.HTTP_200_OK)

# Create your views here.
