from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CandidatViewSet

router = DefaultRouter()
router.register(r'candidats', CandidatViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

from rest_framework import routers
from .views import CandidatViewSet, RecruteurViewSet

router = routers.DefaultRouter()
router.register(r'candidats', CandidatViewSet)
router.register(r'recruteurs', RecruteurViewSet)   # ← ajoute cette ligne

urlpatterns = router.urls
