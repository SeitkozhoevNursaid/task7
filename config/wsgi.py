"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_wsgi_application()

# поднять новое django rest приложение
# Добавить логику:
# - авторизация через почту +
# - 3 роли (сам придумаешь) +
# - пароль должен быть с такими же ограничениями как ты тут делал +
# - сделать сброс пароля +
# - сделать логику "забыл пароль"  +
# - при первичной регистрации отправлять пользователю на почту активационный код, по которому он будет подтверждать себя +

# - serializers переделать
# - token и login понять
# - модельки до ума довести оптимизацию сделать
# - валидация паролей
# - сообщение на почту, разобраться
# - jwt токены last_login разобраться

# - utils.py все переделать
# - блокировать пользователя который не заходил в систему 3 месяца +
# - заставлять менять пароль каждый месяц +

# - добавить возможность сброса пароля в админ панели для пользователей, админом  ???
# - Сохранять все прошлые пароли пользователя, чтобы он не мог обратно менять пароль на прошлый
