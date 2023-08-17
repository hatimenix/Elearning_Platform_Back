"""ecommerce_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework_simplejwt.views import TokenRefreshView
from ecommerce_api import views
from django.conf import settings

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"managers", views.ManagerViewSet, basename="managers")
router.register(r"buyers", views.BuyerViewSet, basename="buyers")
router.register(r"sellers", views.SellerViewSet, basename="sellers")

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
