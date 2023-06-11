from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.



# class Profile(models.Model):
#     AGENT = 2
#     ROLE_CHOICES = (
#         (AGENT, 'Agent'),
#     )
#     user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True)
#     adresse = models.CharField(max_length=30, blank=True,null=True,default="")
#     role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=True, blank=True,default=0)

#     def __str__(self): 
#         return self.user.username

# @receiver(post_save, sender=User)
# def create_or_update_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#     # instance.rofile.save()


class CustomUser(AbstractUser):
    user_type_data=(('1',"ADMIN"), ('2',"STAFF"))
    user_type=models.CharField(default='2',choices=user_type_data,max_length=20)



class Admin(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()


class Staffs(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    address=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()



class Substence(models.Model):
    nom = models.CharField(max_length = 150)
    code = models.CharField(max_length = 150)

    def __str__(self):
        return self.nom 
    

class Client(models.Model):
    nom_entreprise = models.CharField(max_length = 150,null=True,default="")
    registre_de_commerce = models.CharField(max_length = 150,null=True,default="")
    adresse = models.TextField()
    telephone = models.CharField(max_length = 150)


class DataForm(models.Model):
    type_facture = models.CharField(max_length = 150,null=True,default="")
    detenteur = models.ForeignKey(Client, on_delete=models.CASCADE, default=0)
    lieu_extraction = models.CharField(max_length = 200)
    region=models.CharField(max_length = 200,default="",null=True)
    commune = models.CharField(max_length = 200)
    substence = models.ForeignKey(Substence, on_delete=models.CASCADE, default=0)
    montant=models.IntegerField()
    date=models.DateField(auto_now_add=True,null=True)
    

    def __str__(self):
        return self.detenteur


class Attestation(models.Model):
    pass
