from django.contrib.auth.models import User
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from root import settings
import jwt
from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import ListAPIView, GenericAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from apps.users.serializers.auth import LoginSerializer, UserDataSerializer, RegistrationSerializer, \
    EmailVerificationSerializer


class LoginAPIView(TokenObtainPairView):
    """
        DTO
    """
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer


class UserAPIList(ListAPIView):
    """
     DTO
    """
    serializer_class = UserDataSerializer
    queryset = User.objects.all()
    # permission_classes = (IsAuthenticated,)


class RegisterAPIView(GenericAPIView):
    """
     DTO
    """
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
