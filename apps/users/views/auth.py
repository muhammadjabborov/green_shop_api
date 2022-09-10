
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from apps.users.models import User
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
        DAO
    """
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer


class UserAPIList(ListAPIView):
    """
     GET ALL USERS
    """
    serializer_class = UserDataSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)


class RegisterAPIView(GenericAPIView):
    """
     DAO
    """
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# class Logout(GenericAPIView):
#     """
#         DTO
#     """
#     def get(self, request, format=None):
#         request.user.auth_token.delete()
#         return Response(status=status.HTTP_200_OK)
