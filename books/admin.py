from django.contrib import admin
#прописывается скрипт по модели в административную панель, что быпоявлялись новые записи
from.models import *

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Review)
admin.site.register(Favorites)