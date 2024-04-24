from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth.hashers import make_password

from login.models import CustomUser

@receiver(pre_save, sender=CustomUser)
def hash_password(sender, instance, **kwargs):
    user = CustomUser.objects.get(pk=instance.pk)
    if not user.check_password(raw_password=user.password):
        print(f'object password{CustomUser.objects.get(pk=instance.pk).password}')
        instance.password = make_password(instance.password)
        print(f'password{instance.password}')
    
#signals Celery Сортировка 

