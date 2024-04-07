from django.conf import settings
from django.urls import path, include #для нового создания url
from rest_framework.routers import DefaultRouter #подключение роутера(принимает классы ViewSet)
from django.conf.urls.static import static
from .views import *


router = DefaultRouter()
router.register('books',BookViewSet,basename='books')
router.register('author', AuthorViewSet, basename='author')
router.register('genre', GenreViewSet, basename='genre')
router.register('review', ReviewViewSet, basename='review')
router.register('favorites', FavoritesViewSet, basename='favorites')



#зарегистировать новые методы
urlpatterns = [
    path('', include(router.urls)),
    # path("update_cities_ru/", UpdateCityViewSet.as_view({
    #       'get': "update_cities_ru",
    #   })),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #для передачи картинок