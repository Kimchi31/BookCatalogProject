from django.shortcuts import render

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .serializers import *
from .models import *


class TokenObtainPairView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer


class TokenRefreshView(TokenRefreshView):
    serializer_class = TokenRefreshSerializer