
from django import forms

from . models import *

from django.core.validators import RegexValidator


class ClientForm(forms.ModelForm):
   class Meta:
        model = Client
        fields = "__all__"


class SubstenceForm(forms.ModelForm):
   class Meta:
        model = Substence
        fields = "__all__"

# CLIENT_OPTIONS = [(detenteur.id, detenteur) for detenteur in Client.objects.all()]


class ClientDataForm(forms.ModelForm):
   class Meta:
        model = DataForm

        fields="__all__"

        # detenteur = forms.ChoiceField(choices = CLIENT_OPTIONS,  widget=forms.TextInput(attrs={'class': "form-control"}))
        # type_facture = (
        #     ('------------------', '--------------------'),
        #     ('REDEVANCE MINIERE', 'REDEVANCE MINIERE'),
        #     ('DROIT FIXE', 'DROIT FIXE')

        #     )
    #     widgets = {
    #    'type_facture': forms.Select(
    #             choices=type_facture,
    #             attrs={
    #                 'class': 'form-control',
    #             }),
    #      }


class DepotDataForm(forms.ModelForm):
   class Meta:
        model = DataForm

        fields="__all__"

class PaiementDataForm(forms.ModelForm):
   class Meta:
        model = DataForm

        fields="__all__"