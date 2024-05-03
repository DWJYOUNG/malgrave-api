from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CharacterViewSet, generate_presigned_url

router = DefaultRouter()
router.register(r'characters', CharacterViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('generate_presigned_url/', generate_presigned_url, name='generate_presigned_url'),
]
