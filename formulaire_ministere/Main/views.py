from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect

from django.views import View
from django.urls import reverse

from django.shortcuts import redirect,get_object_or_404

from django.contrib import messages

from .forms import *


class IndexView(View):

    template_name="index.html"
        
    def get(self,request, *args, **kwargs):
        return render(request,self.template_name)
    
    def post(self,request, *args, **kwargs):
        return render(request,self.template_name)


class DataView(View):
    template_name="add_formulaire.html"


    
    def get(self,request, *args, **kwargs):
        form = ClientDataForm()
        return render(request,self.template_name,{'form': form})
    
    def post(self,request, *args, **kwargs):
        form = ClientDataForm()
        if request.method == 'POST':
            form = ClientDataForm(data=request.POST)
            if form.is_valid():
                
                form.save()
                messages.success(request, "Formmaire remplit avec success")

                return HttpResponseRedirect('/add_form')
            else:
                form = ClientDataForm()
                messages.success(request, "Echec du remplissage de votre formulaire")

        return render(request, 'formulaire.html', {'form': form})



class ListDataView(View):

    template_name="liste_formulaire.html"

    def get(self,request, *args, **kwargs):
        liste=DataForm.objects.all().order_by("date")
        context={
            'liste':liste,
        }

        return render(request,self.template_name,context)


class ListFormulaireView(View):
    template_name="formulaire.html"

    def get(self,request,dataform_id):
        form=DataForm.objects.get(id=dataform_id)
        context={
            'form':form,
        }

        return render(request,self.template_name,context)



def delete_form(request,dataform_id):
    form = get_object_or_404(DataForm, id=dataform_id)
    form.delete()
    messages.success(request, "Formulaire Supprimer avec success!")
    return HttpResponseRedirect('/liste_formulaire')