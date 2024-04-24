import datetime
from datetime import timedelta
from celery import shared_task

from django.db.models import F, ExpressionWrapper, DurationField
from django.core.mail import send_mail
from django.utils import timezone

from login.models import CustomUser


@shared_task
def send_activation_code(user, code):
    subject = 'Уведомление с http://django'
    message = f'Привет, для подтверждения пожалуйста перейди по ссылке http://127.0.0.1:8000/email-verify/{code}/'
    from_email = 'nursaid.seitkozhoev@mail.ru'
    recipient_list = [user]
    send_mail(subject, message, from_email, recipient_list)


@shared_task
def send_forgot_password(user, code): 
    subject = 'Здравствуйте'
    message =  f'для сброса пароля пожалуйста перейдите по ссылке, http://127.0.0.1:8000/confirm-forgot-password/{code}/'
    from_email = 'nursaid.seitkozhoev@mail.ru'
    recipient_list = [user]
    send_mail(subject, message, from_email, recipient_list)
    

@shared_task
def send_reset_password(user, new_password):
    subject = 'Здравствуйте'          
    message = f'Мы сбросили ваш пароль, ваш новый пароль "{new_password}", с уважением Администрация)'
    from_email = 'nursaid.seitkozhoev@mail.ru'
    recipient_list = [user]
    send_mail(subject, message, from_email, recipient_list)


@shared_task
def block_inactive_users():
    users = CustomUser.objects.annotate(
    time_since_last_login=ExpressionWrapper(
        timezone.now() - F('last_login'),
        output_field=DurationField()
    )
    ).filter(
        is_superuser=False, 
        time_since_last_login__gt=timedelta(days=30)
    )
    users.update(is_active=False)
    print(f"ssssssssssssssssssss{users}")
    for user in users:        
        subject = 'Здравствуйте'
        message = 'Мы заблокировали ваши учетную запись в связи вашим долгим отсутствием)'
        from_email = 'nursaid.seitkozhoev@mail.ru'
        recipient_list = [user.email]
        send_mail(subject, message, from_email, recipient_list)


@shared_task
def notice_change_password_month():
    users = CustomUser.objects.annotate(
    time_since_last_change_password=ExpressionWrapper(
        timezone.now() - F('last_change_password'),
        output_field=DurationField()
    )
    ).filter(
        is_superuser=False, 
        time_since_last_change_password__gt=timedelta(days=20)
    )
    for user in users:
        left_days = datetime.timedelta(days=30) - (timezone.now() - user.date_joined)
        link = f'http://127.0.0.1:8000/change_password/{user.id}/'
        subject = 'Здравствуйте'
        message = f'Ваш пароль почти истек, у вас осталось {left_days}, пожалуйста перейдите по ссылке для смены пароля {link}'
        from_email = 'nursaid.seitkozhoev@mail.ru'
        recipient_list = [user.email]
        send_mail(subject, message, from_email, recipient_list)


@shared_task
def change_password_month():
    users = CustomUser.objects.annotate(
    time_since_last_change_password=ExpressionWrapper(
        timezone.now() - F('last_change_password'),
        output_field=DurationField()
    )
    ).filter(
        is_superuser=False, 
        time_since_last_change_password__gt=timedelta(days=30)
    )
    users.update(is_active=False)
    for user in users:
        subject = 'Здравствуйте'
        message = 'Мы заблокировали ваши учетную запись в связи с тем что вы не поменяли пароль)'
        from_email = 'nursaid.seitkozhoev@mail.ru'
        recipient_list = [user.email]
        send_mail(subject, message, from_email, recipient_list)
