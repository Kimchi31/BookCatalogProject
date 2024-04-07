from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin
)
import random
import string
from django.utils.translation import gettext as _
from django.utils import timezone
import logging

logger=logging.getLogger(__name__)


class UserManager(BaseUserManager):

    def create_user(self, username, password=None):
        user = self.model(username=username)
        user.set_password(password)
        user.role = 2
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(username=username, password=password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.role = 1
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    objects = UserManager()
    ADMIN, USER = range(1, 3)
    ROLE_GROUP = {
        ADMIN: 1,
        USER: 2,
    }

    ROLE_TYPES = (
        (ADMIN, _('Администратор')),
        (USER, _('Пользователь')),
    )

    username = models.CharField('Почта', max_length=50, default='', unique=True)
    phone = models.CharField('Телефон', max_length=50, default='', unique=True, blank=True, null=True)
    name = models.CharField('ФИО', max_length=500, default='', blank=True, null=True)
    role = models.IntegerField('Роль', default=USER, choices=ROLE_TYPES)
    # image = models.ImageField(verbose_name='Аватар', upload_to='user_image', null=True, blank=True)
    is_staff = models.BooleanField(default=False, verbose_name='Доступ в админ панель')
    is_active = models.BooleanField(default=True, verbose_name='Активный аккаунт')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return str(self.username) + ' ' + str(self.name)