

from django.contrib import admin
from django.urls import path
from .views import *

from Main import views

app_name='Main'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('add_form', DataView.as_view(), name='formulaire'),
    path('liste_formulaire/', ListDataView.as_view(), name='liste_formulaire'),
    path('formulaire/<int:dataform_id>', ListFormulaireView.as_view(), name='vue_formulaire'),
    path('formulairedelete/<int:dataform_id>', views.delete_form, name='delete_formulaire'),
]