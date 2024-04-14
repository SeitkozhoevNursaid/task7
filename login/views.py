import jwt
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.conf import settings
from django.core.mail import send_mail

from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from config.tasks import send_notifications
from login.models import CustomUser
from login.serializers import (
    RegistrationSerializer, ChangePasswordSerializer, ForgotPasswordSerializer, ConfirmForgotPasswordSerializer
    )

class RegistrationAPIView(APIView):
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, user.id = serializer.save()
        current_site = get_current_site(request).domain
        link = 'email-verify/'
        print('------------------------------------------------')
        url = f'http://{current_site}/{link}{user.id}/'
        send_notifications(request.data['email'], url)

        return Response('Вам на почту было отправлено письмо с подтверждением вашей регистрации, пожалуйста перейдите по ссылке!', status=status.HTTP_201_CREATED)


class VerifyEmail(APIView):
    def get(self, request, pk):
        user = CustomUser.objects.get(pk=pk)
        user.is_active = True
        user.save()
        return Response('Вы успешно подтвердили регистрацию!')


class ChangePassword(generics.GenericAPIView):
    serializer_class = ChangePasswordSerializer

    def put(self, request, pk):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        password = request.data['password']
        new_password = request.data['new_password']
        print(f"test:       {request.data}")

        obj = CustomUser.objects.get(pk=pk)
        if not obj.check_password(raw_password=password):
            return Response({'Ошибка': 'Пароль не сходится'}, status=400)
        else:
            obj.set_password(new_password)
            obj.save()
            return Response( {'Успешно': 'Вы поменяли пароль'}, status=200)


class ForgotPassword(APIView):
    serializer_class = ForgotPasswordSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        print(f"test22333322:    {serializer}")
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        # user = CustomUser.objects.filter(email=user['email'])
        user = user['email']
        print(f"test222:    {serializer.save()}")
        print(f"test:       {user}")
        current_site = get_current_site(request).domain
        link = 'confirm-forgot-password/'
        url = f'http://{current_site}/{link}{user}/'
        send_mail(
            'Здравствуйте',
            f'для сброса пароля пожалуйста перейдите по ссылке {url})',
            'nursaid.seitkozhoev@mail.ru',
            [user]
            )
        
        return Response('Мы отправили вам письмо на почту с ссылкой на сброс пароля!)')

class ConfirmForgotPassword(APIView):
    serializer_class = ConfirmForgotPasswordSerializer

    def put(self, request, pk):
        user = CustomUser.objects.get(email=pk)
        new_password = request.data['new_password']
        user.set_password(new_password)
        user.save()
        return Response('Вы успешно сменили ваш пароль!)', status=status.HTTP_202_ACCEPTED)        
        