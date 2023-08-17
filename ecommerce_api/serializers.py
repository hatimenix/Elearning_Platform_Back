from rest_framework import serializers
from .models import User,Seller,Buyer,Manager
from rest_framework import serializers
from .models import User,Seller,Buyer,Manager


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