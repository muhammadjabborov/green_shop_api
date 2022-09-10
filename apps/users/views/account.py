from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


from apps.users.serializers.account import ChangeAccountModelSerializer


class ChangeAccountAPIView(GenericAPIView):
    queryset = User.objects.all()
    serializer_class = ChangeAccountModelSerializer
    permission_classes = (IsAuthenticated,)
    parser_classes = (MultiPartParser,)
    lookup_url_kwarg = 'id'

    def put(self, request, pk, *args, **kwargs):
        user = User.objects.get(pk=pk)
        serializer = self.serializer_class(user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = {
            'message': 'Successful update you profile'
        }
        return Response(data, status.HTTP_200_OK)


# class ChangeAccounImageAPIView(GenericAPIView):
#     queryset = UserImage.objects.all()
#     serializer_class = ChangeAccountAvatarModelSerializer
#     permission_classes = (IsAuthenticated,)
#     parser_classes = (MultiPartParser,)
#     lookup_url_kwarg = 'id'
#
#     def put(self, request, pk, *args, **kwargs):
#         user_img = UserImage.objects.get(pk=pk)
#         serializer = ChangeAccountModelSerializer(user_img, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         data = {
#             'message': 'Success'
#         }
#         return Response(data, status.HTTP_200_OK)
