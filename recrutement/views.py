from rest_framework import viewsets
from .models import Candidat
from .serializers import CandidatSerializer

class CandidatViewSet(viewsets.ModelViewSet):
    queryset = Candidat.objects.all()
    serializer_class = CandidatSerializer
