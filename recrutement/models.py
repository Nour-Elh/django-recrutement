from django.db import models

class Candidat(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=20, blank=True)
    cv = models.TextField(blank=True)

    def __str__(self):
        return f"{self.prenom} {self.nom}"
    
class Recruteur(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    entreprise = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nom} ({self.entreprise})"
