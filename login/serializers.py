import re
from rest_framework import serializers
from login.models import CustomUser


class RegistrationSerializer(serializers.Serializer):
    email = serializers.EmailField(
        write_only=True,
    )
    password = serializers.CharField(
        max_length=128,
        min_length=4,
        write_only=True,
    )
    password2 = serializers.CharField(
        max_length=128,
        write_only=True,
    )
    role = serializers.CharField(
        max_length=10,
        write_only=True    
    )

    def validate(self, data):
        if not re.findall('\d', data['password']):
            raise serializers.ValidationError(
                ("В пароле обязательно должна быть 1 цифра"),
            )

        if not re.findall('[A-Z]', data['password']):
            raise serializers.ValidationError(
                ("В пароле обязательно нужна одна буква в верхнем регистре"),
            )

        if not re.findall('[a-z]', data['password']):
            raise serializers.ValidationError(
                ("В пароле обязательно нужна одна буква в нижнем регистре"),
            )

        if not re.findall('[()[\]{}|\\`~!@#$%^&*_\-+=;:\'",<>./?]', data['password']):
            raise serializers.ValidationError(
                ("В пароле должен быть 1 символ"),
            )

        if data['password'] != data['password2']:
            raise serializers.ValidationError(
                ('Пароли не совпадают')
            )
        # data1= data.pop('password2') # pop !!!!!!!!!!!!!!!!!!!!
        
        return data

    def create(self, validated_data):
        password2 = validated_data.pop('password2')
        user = CustomUser.objects.create_user(**validated_data)
        user.is_active = False
        user.save()
        return user, user.id
    
    def update(self, instance, validated_data):
        return instance



class ChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)

    def validate(self, data):
        if data['new_password'] != data['confirm_password']:
            raise serializers.ValidationError(
                ('Пароли не совпадают')
            )
        return data

    def create(self, validated_data):
        print(f'validated_data:       {validated_data}')
        return validated_data
    
    def update(self, instance, validated_data):
        print(f'aaaaaaaaaa{instance}')
        return instance


class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)

    def create(self, validated_data):
        print(f'validated_data:       {validated_data}')
        return validated_data
    
    def update(self, instance, validated_data):
        print(f'aaaaaaaaaa{instance}')
        return instance
        


class ConfirmForgotPasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)

    def validate(self, data):
        if data['new_password'] != data['confirm_password']:
            raise serializers.ValidationError(
                ('Пароли не совпадают')
            )
        return data