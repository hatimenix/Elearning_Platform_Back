from django.shortcuts import render
from rest_framework.response import Response
from .models import User,Manager,Seller,Buyer,Category, Article, Favori , Properties
from .serializers import UserSer,ManagerSer,SellerSer,BuyerSer,CategorySerializer, ArticleSerializer, FavoriSerializer , PropertiesSerializer
from rest_framework import permissions ,viewsets ,status
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from django.contrib.auth.hashers import check_password
from rest_framework.views import APIView
from rest_framework import viewsets, filters


class UserView(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticatedOrDenied]
    permission_classes = [AllowAny]
    serializer_class = UserSer
    queryset = User.objects.all()

class SellerViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticatedOrDenied]
    permission_classes = [AllowAny]
    serializer_class = SellerSer
    queryset = Seller.objects.all()    

class BuyerViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticatedOrDenied]
    permission_classes = [AllowAny]
    serializer_class = BuyerSer
    queryset = Buyer.objects.all()    
    
class ManagerViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticatedOrDenied]
    permission_classes = [AllowAny]
    serializer_class = ManagerSer
    queryset = Manager.objects.all()        
    
#manager login    
class ManagerTokenObtainPairView(TokenObtainPairView):
    # permission_classes = [IsAuthenticatedOrDenied]
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):

        email = request.data.get("email")
        password = request.data.get("password")

        Usercode = User.objects.get(email=email)
        user=Usercode.manager

        code = user.code

        if check_password(password, Usercode.password):
            code = Usercode.code

        else :
            code ="123"
            return Response(
                        {"message": "Mot de passe incorrect"},
                        status=status.HTTP_400_BAD_REQUEST,
                    )    
        try:
            user = User.objects.select_related("manager").get(code=code)
            manager = user.manager

            if manager and manager.etat:
                if check_password(password, user.password):
                    refresh = RefreshToken.for_user(user)
                    return Response(
                        {
                            "access": str(refresh.access_token),
                            "role": manager.role,
                            "refresh": str(refresh),
                        }
                    )
                else:
                    return Response(
                        {"message": "Mot de passe incorrect"},
                        status=status.HTTP_400_BAD_REQUEST,
                    )
            else:
                return Response(
                    {"message": "votre compte est désactivé"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

        except User.DoesNotExist:

            return Response(
                {"message": "Email incorrect"},
                status=status.HTTP_400_BAD_REQUEST,
            )

#Seller login    
class SellerTokenObtainPairView(TokenObtainPairView):
    # permission_classes = [IsAuthenticatedOrDenied]
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):

        email = request.data.get("email")
        password = request.data.get("password")
        Usercode = Seller.objects.get(email=email)
        code = Usercode.code

        if check_password(password, Usercode.password):
            code = Usercode.code

        else :
            code ="123"  
            return Response(
                        {"message": "Mot de passe incorrect"},
                        status=status.HTTP_400_BAD_REQUEST,
                    )      
        try:
            user = User.objects.select_related("seller").get(code=code)
            seller = user.seller
            if seller and seller.etat:
                if check_password(password, user.password):
                    refresh = RefreshToken.for_user(user)
                    return Response(
                        {
                            "access": str(refresh.access_token),
                            "refresh": str(refresh),
                        }
                    )
                else:
                    return Response(
                        {"message": "Mot de passe incorrect"},
                        status=status.HTTP_400_BAD_REQUEST,
                    )
            else:
                return Response(
                    {"message": "votre compte est désactivé"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        except User.DoesNotExist:
            return Response(
                {"message": "Email incorrect"},
                status=status.HTTP_400_BAD_REQUEST,
            )

#Buyer login    
class BuyerTokenObtainPairView(TokenObtainPairView):
    # permission_classes = [IsAuthenticatedOrDenied]
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):

        email = request.data.get("email")
        password = request.data.get("password")
        Usercode = Buyer.objects.get(email=email)
        code = Usercode.code

        if check_password(password, Usercode.password):
            code = Usercode.code

        else :
            code ="123"  
            return Response(
                        {"message": "Mot de passe incorrect"},
                        status=status.HTTP_400_BAD_REQUEST,
                    )      
        try:
            user = User.objects.select_related("buyer").get(code=code)
            buyer = user.buyer
            if buyer and buyer.etat:
                if check_password(password, user.password):
                    refresh = RefreshToken.for_user(user)
                    return Response(
                        {
                            "access": str(refresh.access_token),
                            "refresh": str(refresh),
                        }
                    )
                else:
                    return Response(
                        {"message": "Mot de passe incorrect"},
                        status=status.HTTP_400_BAD_REQUEST,
                    )
            else:
                return Response(
                    {"message": "votre compte est désactivé"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        except User.DoesNotExist:
            return Response(
                {"message": "Email incorrect"},
                status=status.HTTP_400_BAD_REQUEST,
            )

class UserDetailsAPIView(APIView):
    # permission_classes = [IsAuthenticatedOrDenied]
    permission_classes = [AllowAny]
    def get(self, request):
        user = request.user
        serializer = UserSer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


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
