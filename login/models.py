from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.contrib.auth.hashers import make_password


class CustomManager(UserManager):

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Укажите почту')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField("email", max_length=254, unique=True)
    objects = CustomManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Role(models.TextChoices):
        BUYER = 'buyer', 'Buyer'
        SELLER = 'seller', 'Seller'        

    role = models.CharField(choices=Role.choices)
    last_login = models.DateTimeField(auto_now=True)
    last_active = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email
