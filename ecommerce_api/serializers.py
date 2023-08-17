from rest_framework import serializers
from .models import Category, Article, Favori , Properties

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ArticleSerializer(serializers.ModelSerializer):
    favoris = serializers.PrimaryKeyRelatedField(many=True, queryset=Favori.objects.all(), required=False)

    class Meta:
        model = Article
        fields = '__all__'

class FavoriSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favori
        fields = '__all__'


class PropertiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Properties
        fields = '__all__'
