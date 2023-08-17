from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from ecommerce_api.views import CategoryViewSet, ArticleViewSet, FavoriViewSet , PropertiesViewSet
from rest_framework import routers
from django.conf.urls.static import static

from ecommerce_backend import settings


router = routers.DefaultRouter()
router.register(r"categories", CategoryViewSet, basename="category")
router.register(r"articles", ArticleViewSet, basename="article")
router.register(r"favoris", FavoriViewSet, basename="favori")
router.register(r"properties", PropertiesViewSet, basename="properties")


urlpatterns = [
       path("admin/", admin.site.urls),
    path('', include(router.urls)),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
