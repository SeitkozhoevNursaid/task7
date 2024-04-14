import schedule
import datetime
import threading
import random
import string
from datetime import timedelta
from celery import shared_task

from django.core.mail import send_mail
from django.utils import timezone

from login.models import CustomUser


def send_notifications(user, url):
    subject = 'Уведомление с http://django'
    message = f'Привет, для подтверждения пожалуйста перейди по ссылке {url}'
    from_email = 'nursaid.seitkozhoev@mail.ru'
    recipient_list = [user]
    mail_sent = send_mail(subject, message, from_email, recipient_list)
    return mail_sent


@shared_task
def delete_inactive_users():
    users_to_delete = []
    users = CustomUser.objects.filter(is_superuser=False)
    print(f"test:::::    {users}")
    for user in users:
        if timezone.now() - user.last_active > timedelta(minutes=2):
            users_to_delete.append(user.pk)
    CustomUser.objects.filter(pk__in=users_to_delete).delete()


@shared_task
def change_password_month():
    print('fffffffffffffffffffffffffffffff')
    users = CustomUser.objects.filter(is_superuser=False)
    for user in users:
        if timezone.now() - user.date_joined > datetime.timedelta(days=20):
            left_days = datetime.timedelta(days=30) - (timezone.now() - user.date_joined)
            link = f'http://127.0.0.1:8000/change_password/{user.id}/'
            print(f"trst:::      {left_days}")
            subject = 'Здравствуйте'
            message = f'Ваш пароль почти истек, у вас осталось {left_days}, пожалуйста перейдите по ссылке для смены пароля {link}'
            from_email = 'nursaid.seitkozhoev@mail.ru'
            recipient_list = [user.email]
            send_mail(subject, message, from_email, recipient_list)
            
            # if timezone.now() - user.date_joined > datetime.timedelta(minutes=3):
            



#Блокировать
