from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from apps.users.views.addres import AddresModelViewSet
from apps.users.views.auth import LoginAPIView, RegisterAPIView, UserAPIList

router = DefaultRouter()

router.register('', AddresModelViewSet)

urlpatterns = [
    path('user/login/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('user/login/', LoginAPIView.as_view(), name='token_obtain_pair'),
    path('user/register/', RegisterAPIView.as_view(), name='register'),
    path('user/billing-addres/', include(router.urls),name='billing-addres'),
    path('user/api-list/',UserAPIList.as_view(),name='user-api-list')
]
