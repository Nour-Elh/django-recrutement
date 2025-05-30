from rest_framework import viewsets
from .models import Candidat
from .serializers import CandidatSerializer

class CandidatViewSet(viewsets.ModelViewSet):
    queryset = Candidat.objects.all()
    serializer_class = CandidatSerializer
    
from .models import Recruteur
from .serializers import RecruteurSerializer
from rest_framework import viewsets

class RecruteurViewSet(viewsets.ModelViewSet):
    queryset = Recruteur.objects.all()
    serializer_class = RecruteurSerializer
