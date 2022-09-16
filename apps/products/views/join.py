from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from apps.products.models import JoinUser
from apps.products.serializers.join import JoinModelSerializer
from apps.products.service import Util


class JoinAPIView(GenericAPIView):
    serializer_class = JoinModelSerializer
    queryset = JoinUser.objects.all()
    # permission_classes = (IsAuthenticated,)
    # pagination_class = JoinUserPagination
    parser_classes = (MultiPartParser,)

    def post(self, request):
        """
        JOIN NEW USERS AFTER THAT USERS WILL SEND AUTHENICATION MESSAGE
        :param request:
        :return:
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        Util.send_email(serializer.validated_data.get('email'))
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request, *args, **kwargs):
        """
        GET ALL JOINED USERS
        """
        join_users = self.queryset.all()
        serializer = self.serializer_class(join_users, many=True)
        return Response(serializer.data)
