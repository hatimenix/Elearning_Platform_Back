from rest_framework import serializers
from .models import User,Seller,Buyer,Manager
from rest_framework import serializers
from .models import User,Seller,Buyer,Manager,Category, Article, Favori , Properties

class UserSer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"

class SellerSer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = "__all__"

class BuyerSer(serializers.ModelSerializer):
    class Meta:
        model = Buyer
        fields = "__all__"

class ManagerSer(serializers.ModelSerializer):
    role = serializers.CharField(source="manager.role", read_only=True)
    class Meta:
        model = Manager
        fields = "__all__"

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
