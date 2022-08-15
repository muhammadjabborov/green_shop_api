from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from app.products.models import JoinUser
from app.products.serializers.join import JoinModelSerializer
from app.products.service import Util
from app.shared.rest_framework.pagination import JoinUserPagination


class JoinAPIView(GenericAPIView):
    serializer_class = JoinModelSerializer
    queryset = JoinUser.objects.all()
    permission_classes = (IsAuthenticated,)
    pagination_class = JoinUserPagination
    parser_classes = (MultiPartParser,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            Util.send_email(serializer.validated_data.get('email'))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        join_users = self.queryset.all()
        serializer = self.serializer_class(join_users, many=True)
        return Response(serializer.data)
