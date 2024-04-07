from django.conf import settings
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from .views import *

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    # path("update_cities_ru/", UpdateCityViewSet.as_view({
    #       'get': "update_cities_ru",
    #   })),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)