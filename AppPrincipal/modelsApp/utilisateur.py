from django.db import models


class Utilisateur(models.Model):
    nom = models.CharField(max_length=20)
    password = models.CharField(max_length=20)