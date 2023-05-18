from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.query import QuerySet

from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.



class FullUser(AbstractUser):
      class Role(models.TextChoices):

        STAFF = (
            "STAFF",
            "STAFF",
        )

      base_role = Role.STAFF
      role = models.CharField(max_length=50, choices=Role.choices, default="", null=True)

      def save(self, *args, **kwargs):
            if not self.pk:
                self.role = self.base_role

            return super().save(*args, **kwargs)
    

class StaffManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        resultat = super().get_queryset(*args, **kwargs)
        return resultat.filter(role=FullUser.Role.STAFF)


class Staff(FullUser):
    base_role = FullUser.Role.STAFF

    staff = StaffManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Bonjour Staff"
    

@receiver(post_save, sender=Staff)

def create_user_profile(sender,instance,created, **kwargs):
    if created and instance.role=="STAFF":
        StaffProfil.objects.create(user=instance)



class StaffProfil(models.Model):
    user = models.OneToOneField(FullUser, on_delete=models.CASCADE,null=True)
    staff_id=models.IntegerField(null=True, blank=True, default=1)
    




class DataForm(models.Model):
    detenteur = models.CharField(max_length = 200)
    lieu_extraction = models.CharField(max_length = 200)
    commune = models.CharField(max_length = 200)
    substence = models.CharField(max_length = 200)
    montant=models.IntegerField()
    date=models.DateField(auto_now_add=True,null=True)
    

    def __str__(self):
        return self.detenteur


