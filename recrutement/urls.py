from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CandidatViewSet

router = DefaultRouter()
router.register(r'candidats', CandidatViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
