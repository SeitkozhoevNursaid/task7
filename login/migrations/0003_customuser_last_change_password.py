# Generated by Django 5.0.4 on 2024-04-18 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_alter_customuser_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='last_change_password',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
