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

from apps.users.models import User
from apps.users.serializers import LoginSerializer, UserDataSerializer, RegistrationSerializer


class LoginAPIView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer


class UserAPIList(ListAPIView):
    serializer_class = UserDataSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)


class RegisterAPIView(GenericAPIView):
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
