
from django import forms

from . models import *

from django.core.validators import RegexValidator

class ClientDataForm(forms.ModelForm):

   detenteur = forms.CharField(required=True)
   lieu_extraction = forms.CharField(max_length=1000)
   commune = forms.CharField(max_length=1000)
   substence = forms.CharField(max_length=1000)
   montant= forms.IntegerField()

   class Meta:
        model = DataForm
        fields = "__all__"