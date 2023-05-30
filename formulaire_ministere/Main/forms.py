
from django import forms

from . models import *

from django.core.validators import RegexValidator


class ClientForm(forms.ModelForm):
   prenom = forms.CharField(required=True)
   nom = forms.CharField(max_length=1000)
   adresse = forms.CharField(max_length = 150,widget=forms.Textarea)
   telephone = forms.CharField(max_length=1000)


   class Meta:
        model = Client
        fields = "__all__"

CLIENT_OPTIONS = [(detenteur.id, detenteur) for detenteur in Client.objects.all()]


class ClientDataForm(forms.ModelForm):
   lieu_extraction = forms.CharField(max_length=1000,required=True)
   commune = forms.CharField(max_length=1000,required=True)
   substence = forms.CharField(max_length=1000,required=True)
   montant= forms.IntegerField(required=True)

   class Meta:
        model = DataForm

        fields="__all__"

        detenteur = forms.ChoiceField(choices = CLIENT_OPTIONS,  widget=forms.TextInput(attrs={'class': "form-control"}))
        type_facture = (
            ('------------------', '--------------------'),
            ('REDEVANCE MINIERE', 'REDEVANCE MINIERE'),
            ('DROIT FIXE', 'DROIT FIXE')

            )
        widgets = {
       'type_facture': forms.Select(
                choices=type_facture,
                attrs={
                    'class': 'form-control',
                }),
         }