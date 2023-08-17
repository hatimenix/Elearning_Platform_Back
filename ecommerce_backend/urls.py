from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework_simplejwt.views import TokenRefreshView
from ecommerce_api import views
from django.conf import settings
from rest_framework import routers
from ecommerce_api.views import CategoryViewSet, ArticleViewSet, FavoriViewSet , PropertiesViewSet

from ecommerce_backend import settings

router = routers.DefaultRouter()
router.register(r"managers", views.ManagerViewSet, basename="managers")
router.register(r"buyers", views.BuyerViewSet, basename="buyers")
router.register(r"sellers", views.SellerViewSet, basename="sellers")
router.register(r"categories", CategoryViewSet, basename="category")
router.register(r"articles", ArticleViewSet, basename="article")
router.register(r"favoris", FavoriViewSet, basename="favori")
router.register(r"properties", PropertiesViewSet, basename="properties")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),

    path("token/buyer/",views.BuyerTokenObtainPairView.as_view(),name="buyer_token_obtain_pair"),
    path("token/seller/",views.SellerTokenObtainPairView.as_view(),name="seller_token_obtain_pair"),
    path("token/manager/",views.ManagerTokenObtainPairView.as_view(),name="manager_token_obtain_pair"),

    path("token/seller/refresh/", TokenRefreshView.as_view(),name="seller_token_refresh" ),
    path("token/buyer/refresh/", TokenRefreshView.as_view(),name="buyer_token_refresh" ),
    path("token/manager/refresh/", TokenRefreshView.as_view(),name="manager_token_refresh" ),

    path("auth/user/", views.UserDetailsAPIView.as_view(), name="user_detail"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
