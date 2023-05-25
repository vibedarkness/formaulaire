from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.



class FullUser(AbstractUser):
    pass
    

class Client(models.Model):
    prenom = models.CharField(max_length = 150)
    nom = models.CharField(max_length = 150)
    adresse = models.TextField()
    telephone = models.CharField(max_length = 150)


class DataForm(models.Model):
    type_facture = models.CharField(max_length = 150,null=True,default="")
    detenteur = models.ForeignKey(Client, on_delete=models.CASCADE, default=0)
    lieu_extraction = models.CharField(max_length = 200)
    commune = models.CharField(max_length = 200)
    substence = models.CharField(max_length = 200)
    montant=models.IntegerField()
    date=models.DateField(auto_now_add=True,null=True)
    

    def __str__(self):
        return self.detenteur


class Attestation(models.Model):
    pass
