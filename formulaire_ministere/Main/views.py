from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from Main.EmailBackend import EmailBackend
from django.contrib.auth.decorators import login_required

from django.views import View
from django.urls import reverse

from django.shortcuts import redirect,get_object_or_404

from django.contrib import messages

from .forms import *



class ClientView(View):
    template_name="add_client.html"
    
    

    def get(self,request, *args, **kwargs):
        form = ClientForm()
        return render(request,self.template_name,{'form': form})
    
    def post(self,request, *args, **kwargs):
        form = ClientForm()
        if request.method == 'POST':
            form = ClientForm(data=request.POST)
            if form.is_valid():
                
                form.save()
                messages.success(request, "Formmaire remplit avec success")

                return HttpResponseRedirect('/add_client')
            else:
                form = ClientForm()
                messages.success(request, "Echec du remplissage de votre formulaire")

        return render(request,'add_client.html', {'form': form})





class IndexView(View):

    template_name="index.html"

    client=Client.objects.all()

    context={
        'client':client,
    }
        
    def get(self,request, *args, **kwargs):
        return render(request,self.template_name,self.context)
    
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



def do_login(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        user=EmailBackend.authenticate(request,username=request.POST.get("email"),password=request.POST.get("password"))
        if user!=None:
            login(request)
            if user.user_type=="1":
                return HttpResponseRedirect('/admin')
            
            elif user.user_type=="2":
                return HttpResponseRedirect(reverse("index"))
            else:
                return HttpResponse("dingo")

        else:
            messages.error(request,"Email ou mot de passe invalide")
            return HttpResponseRedirect("/")
