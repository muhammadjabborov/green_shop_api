from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from apps.users.views import LoginAPIView, RegisterAPIView

urlpatterns = [
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('login/', LoginAPIView.as_view(), name='token_obtain_pair'),
    path('register/', RegisterAPIView.as_view(), name='register'),
    # path('verify-email/',VerifyEmail.as_view(),name='email-verify')
]
