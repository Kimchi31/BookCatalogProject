from django.shortcuts import render
#контроллеры

from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet, mixins, ReadOnlyModelViewSet
from rest_framework import status




class AuthorViewSet(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewSet(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny | IsAuthenticated]


class GenreViewSet(ReadOnlyModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer



class FavoritesViewSet(GenericViewSet, mixins.ListModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.CreateModelMixin):
    queryset = Favorites.objects.all()
    serializer_class = FavoritesSerializer
    permission_classes = [IsAuthenticated]



    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(Favorites.objects.filter(user=request.user))

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


    def create(self, request, *args, **kwargs):
        # serializer = self.get_serializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # self.perform_create(serializer)
        # headers = self.get_success_headers(serializer.data)
        # return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


        user = request.user
        user.id = user.id
        try:
            book = Book.objects.get(id=request.data['book'])

        except:
            return Response ({"error": "book not found"}, status=status.HTTP_404_NOT_FOUND)
        favorite = Favorites.objects.create(user=user, book=book)
        return Response({"status" : "okay"})