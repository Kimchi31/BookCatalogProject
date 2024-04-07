from .models import *
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from django.core.exceptions import ObjectDoesNotExist
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import (
    TokenRefreshSerializer, TokenObtainPairSerializer)
from rest_framework_simplejwt.exceptions import AuthenticationFailed
from django.conf import settings


class TokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        username = attrs.get(self.username_field)
        attrs[self.username_field] = username

        data = super().validate(attrs)

        if not self.user.is_active:
            raise AuthenticationFailed({
                'detail': f"Пользователь {self.user.username} был деактивирован!"
            }, code='user_blocked')

        # elif self.user.is_active in ['incorrect_document', 'upload_document']:
        #     raise AuthenticationFailed({
        #         'detail': f"Пользователь {self.user.username} не прошел проверку документов!",
        #         'username': self.user.username
        #     }, code='user_not_approved')

        data['id'] = self.user.id
        data['username'] = self.user.username
        data['role'] = self.user.ROLE_GROUP[self.user.role]
        user = self.user
        user.save()

        return data


class TokenRefreshSerializer(TokenRefreshSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = RefreshToken(attrs['refresh'])

        try:
            user = User.objects.get(
                pk=refresh.payload.get('user_id')
            )
        except ObjectDoesNotExist:
            raise serializers.ValidationError({
                'detail': f"Пользователь был удалён!"
            }, code='user_does_not_exists')

        if not user.is_active:
            raise AuthenticationFailed({
                'detail': f"Пользователь {self.user.username} был деактивирован!"
            }, code='user_blocked')

        # elif user.is_active in ['incorrect_document', 'upload_document']:
        #     raise AuthenticationFailed({
        #         'detail': f"Пользователь {self.user.username} не прошел проверку документов!", 'username': user.username
        #     }, code='user_not_approved')

        data['id'] = user.id
        data['username'] = user.username
        data['role'] = user.ROLE_GROUP[user.role]

        return data