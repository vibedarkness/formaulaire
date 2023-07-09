

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
    path('formulaireupdate/<int:data_id>', views.update_facture, name='update_facture'),    


    #-----------------Client urls-------------------------------
    path('add_client', ClientView.as_view(), name='add_client'),
    path('client', ListDataView.as_view(), name='client'),
    path('clientdelete/<int:client_id>', views.delete_client, name='delete_client'),
    path('clientupdate/<int:client_id>', views.update_client, name='update_client'),

    #-----------------Substence urls-------------------------------
    path('substence', SubstenceDataView.as_view(), name='substence'),
    path('add_substence', SubstenceView.as_view(), name='add_substence'),
    path('substencedelete/<int:substence_id>', views.delete_substence, name='delete_substence'),
    path('substenceupdate/<int:substence_id>', views.update_substence, name='update_substence'),

    #-----------------Attestation depôt urls-------------------------------

    path('add_attestation_depot', AttestationDepotView.as_view(), name='depot'),
    path('liste_attestation_depot/', ListDepotView.as_view(), name='attestation_depot'),
    path('attestation_depot_view/<int:datadepot_id>', DepotView.as_view(), name='attestation_depot_view'),

    #-----------------Attestation paiement urls-------------------------------

    path('add_attestation_paiement', AttestationPaiementView.as_view(), name='paiement'),
    path('liste_attestation_paiement/', ListPaiementView.as_view(), name='attestation_paiement'),
    path('attestation_paiement_view/<int:datapaiement_id>', PaiementView.as_view(), name='attestation_paiement_view'),






]