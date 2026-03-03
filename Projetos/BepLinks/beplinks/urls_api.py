from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views_api import TemaViewSet, RecursoViewSet

router = DefaultRouter()
router.register(r'temas', TemaViewSet, basename='tema')
router.register(r'recursos', RecursoViewSet, basename='recurso')

urlpatterns = [
    path('', include(router.urls)),
]
