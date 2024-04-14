from django.urls import path, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from login.views import RegistrationAPIView, VerifyEmail, ChangePassword, ForgotPassword, ConfirmForgotPassword

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    re_path('registration/', RegistrationAPIView.as_view(), name='registration'),
    path('email-verify/<int:pk>/', VerifyEmail.as_view(), name='email-verify'),
    path('change_password/<int:pk>/', ChangePassword.as_view(), name='change_password'),
    path('forgot-password/', ForgotPassword.as_view()),
    path('confirm-forgot-password/<str:pk>/', ConfirmForgotPassword.as_view())
]