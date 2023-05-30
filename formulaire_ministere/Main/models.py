from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.



class FullUser(AbstractUser):
    user_type_data=((1,"ADMIN"), (2,"STAFF"))
    user_type=models.CharField(default=1,choices=user_type_data,max_length=20)


class Admin(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(FullUser,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()


class Staff(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(FullUser,on_delete=models.CASCADE)
    address=models.TextField()
    telephone = models.CharField(max_length = 150)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

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
