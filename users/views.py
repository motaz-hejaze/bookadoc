from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView
from rest_framework import permissions
from .serializers import CustomUserSerializer
# Create your views here.

class HomeView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {
            'message':'Hello, World'
        }
        return Response(content)



class Register(CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = CustomUserSerializer

    