from django.db import models
from BookCatalogProject.authorization.models import User


#модели специальные классы, которые отрисовывают
#нужны для подключения к бд 


class Author (models.Model):
    f_name = models.CharField(verbose_name='Имя', max_length=255)
    l_name = models.CharField(verbose_name='Фамилия', null=True, blank=True, max_length=255)

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return str(self.f_name) + str(self.l_name)

class Book (models.Model):
    name = models.CharField(verbose_name='Название', max_length=255)
    description= models.TextField(verbose_name='Описание', null=True, blank=True)
    author = models.ForeignKey(Author, verbose_name='Автор', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(verbose_name='Название', max_length=255)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name


class Review(models.Model):
    book = models.ForeignKey(Book,verbose_name='Отзывы', on_delete=models.CASCADE)
    rating = models.IntegerField(default=5, verbose_name="Рейтинг отзыва")
    review = models.TextField(verbose_name="Отзыв")


class Favorites(models.Model):
    # user = models.OneToOneField()
    user = models.ForeignKey(User,verbose_name="Пользователь", on_delete=models.CASCADE)
    book = models.ForeignKey(Book, verbose_name="Избранная книга", on_delete=models.CASCADE)








