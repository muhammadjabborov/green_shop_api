from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from apps.products.models import JoinUser
from apps.products.serializers.join import JoinModelSerializer
from apps.products.service import Util

from apps.shared.rest_framework.pagination import JoinUserPagination


class JoinAPIView(GenericAPIView):
    serializer_class = JoinModelSerializer
    queryset = JoinUser.objects.all()
    # permission_classes = (IsAuthenticated,)
    pagination_class = JoinUserPagination
    parser_classes = (MultiPartParser,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        Util.send_email(serializer.validated_data.get('email'))
        return Response(serializer.data, status=status.HTTP_201_CREATED)


def get(self, request, *args, **kwargs):
    join_users = self.queryset.all()
    serializer = self.serializer_class(join_users, many=True)
    return Response(serializer.data)
