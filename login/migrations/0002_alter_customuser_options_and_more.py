# Generated by Django 5.0.4 on 2024-04-17 04:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.RenameField(
            model_name='userpasswords',
            old_name='passwords',
            new_name='password',
        ),
    ]
