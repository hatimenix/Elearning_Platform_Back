from rest_framework import viewsets, filters
from .models import Category, Article, Favori , Properties
from .serializers import CategorySerializer, ArticleSerializer, FavoriSerializer , PropertiesSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['id_cat', 'titre']  # Add more fields if needed

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['id_art', 'titre', 'description']  # Add more fields if needed

class FavoriViewSet(viewsets.ModelViewSet):
    queryset = Favori.objects.all()
    serializer_class = FavoriSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['id_fav']  # Add more fields if needed
class PropertiesViewSet(viewsets.ModelViewSet):
    queryset = Properties.objects.all()
    serializer_class = PropertiesSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['id_pro']  # Add more fields if needed
