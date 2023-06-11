

from django.contrib import admin
from django.urls import path
from .views import *
# from django.contrib.auth.decorators import login_required

from Main import views

app_name='Main'

urlpatterns = [
    #-----------------Login urls-------------------------------
    path('loginapp', views.loginapp, name='loginapp'),
    path('dologin', views.do_login, name='dologin'),
    path('logout_user', views.logout_user,name="logout_user"),

    
    #-----------------Acceuil urls-------------------------------
    path('', AcceuilView.as_view(), name='acceuil'),

    #-----------------Facture urls-------------------------------    
    path('liste_formulaire/', IndexView.as_view(), name='facture'),
    path('add_form', DataView.as_view(), name='formulaire'),
    path('formulaire/<int:dataform_id>', ListFormulaireView.as_view(), name='vue_formulaire'),
    path('formulairedelete/<int:dataform_id>', views.delete_form, name='delete_formulaire'),


    #-----------------Client urls-------------------------------
    path('add_client', ClientView.as_view(), name='add_client'),
    path('client', ListDataView.as_view(), name='client'),
    path('clientdelete/<int:client_id>', views.delete_client, name='delete_client'),

    #-----------------Substence urls-------------------------------
    path('substence', SubstenceDataView.as_view(), name='substence'),
    path('add_substence', SubstenceView.as_view(), name='add_substence'),
    path('substencedelete/<int:substence_id>', views.delete_substence, name='delete_substence'),





]