from django.urls import path, re_path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from login.views import (
    RegistrationAPIView,
    VerifyEmail,
    ChangePassword,
    ForgotPassword,
    ConfirmForgotPassword,
    AdminResetPassword,
)

urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),  # TODO: ...
    path('token/refresh/', TokenRefreshView.as_view()),
    re_path('registration/', RegistrationAPIView.as_view()),
    path('email-verify/<uuid:activation_code>/', VerifyEmail.as_view()),
    path('change_password/', ChangePassword.as_view()),
    path('forgot-password/', ForgotPassword.as_view()),
    path('confirm-forgot-password/<str:pk>/', ConfirmForgotPassword.as_view()),
    path('reset_password/', AdminResetPassword.as_view())
]
