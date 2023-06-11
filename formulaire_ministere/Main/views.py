from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from Main.EmailBackend import EmailBackend
from django.contrib.auth.decorators import login_required

from django.views import View
from django.urls import reverse

from django.shortcuts import redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


from django.contrib import messages

from .forms import *



def loginapp(request):
    return render(request,"login.html")




class AcceuilView(View):
    template_name="acceuil.html"

    client=Client.objects.all().count
    facture=DataForm.objects.all().count
    substence=Substence.objects.all().count

    context={
        'total_client':client,
        'total_facture':facture,
        'total_substence':substence
    }
    # @login_required(login_url='loginapp')
    @method_decorator(login_required(login_url='Main:loginapp'))    
    def get(self,request, *args, **kwargs):
        return render(request,self.template_name,self.context)
    
    def post(self,request, *args, **kwargs):
        return render(request,self.template_name)



class SubstenceDataView(View):
    template_name="substence.html"

    substence=Substence.objects.all()


    context={
        'substence':substence,

    }
    
    @method_decorator(login_required(login_url='Main:loginapp'))
        
    def get(self,request, *args, **kwargs):
        return render(request,self.template_name,self.context)
    
    def post(self,request, *args, **kwargs):
        return render(request,self.template_name)


class ClientView(View):
    template_name="add_client.html"
    
    
    @method_decorator(login_required(login_url='Main:loginapp'))
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

                return HttpResponseRedirect("/client")
            else:
                form = ClientForm()
                messages.success(request, "Echec du remplissage de votre formulaire")

        return render(request,'add_client.html', {'form': form})



class SubstenceView(View):
    template_name="add_substence.html"
    
    
    @method_decorator(login_required(login_url='Main:loginapp'))
    def get(self,request, *args, **kwargs):
        form = SubstenceForm()
        return render(request,self.template_name,{'form': form})
    
    def post(self,request, *args, **kwargs):
        form = ClientForm()
        if request.method == 'POST':
            form = SubstenceForm(data=request.POST)
            if form.is_valid():
                
                form.save()
                messages.success(request, "Formmaire remplit avec success")

                return HttpResponseRedirect("/add_substence")
            else:
                form = SubstenceForm()
                messages.success(request, "Echec du remplissage de votre formulaire")

        return render(request,'add_substence.html', {'form': form})



class IndexView(View):

    template_name="liste_formulaire.html"

    @method_decorator(login_required(login_url='Main:loginapp'))
    def get(self,request, *args, **kwargs):
        liste=DataForm.objects.all().order_by("date")
        context={
            'liste':liste,
        }

        return render(request,self.template_name,context)






class DataView(View):


    template_name="add_formulaire.html"


    @method_decorator(login_required(login_url='Main:loginapp'))
    
    def get(self,request, *args, **kwargs):
        form = ClientDataForm()
        detenteur=Client.objects.all()
        substence=Substence.objects.all()
        context={
           'detenteur':detenteur,
           'form' :form,
           'substence':substence,
        }
        return render(request,self.template_name,context)
    
    def post(self,request, *args, **kwargs):
       if request.method=="POST":
            type_facture=request.POST.get("type")
            detenteur=request.POST.get("detenteur")
            region=request.POST.get("region")
            substence=request.POST.get("substence")
            commune=request.POST.get("commune")
            montant=request.POST.get("montant")
            lieu=request.POST.get("lieu")
            try:
                facture=DataForm(type_facture=type_facture,detenteur_id=detenteur,region=region,substence_id=substence,commune=commune,montant=montant,lieu_extraction=lieu)
                facture.save()
                messages.success(request,"Ajout avec Success")
                return HttpResponseRedirect(reverse("Main:formulaire"))
            except Exception as e :
                messages.error(request, "Pas d'ajout " + str(e))
                print(e)
                return HttpResponseRedirect(reverse("Main:formulaire"))




class ListDataView(View):
    template_name="index.html"

    client=Client.objects.all()

    context={
        'client':client,
    }
    
    @method_decorator(login_required(login_url='Main:loginapp'))    
    def get(self,request, *args, **kwargs):
        return render(request,self.template_name,self.context)
    
    def post(self,request, *args, **kwargs):
        return render(request,self.template_name)


class ListFormulaireView(View):

    template_name="formulaire.html"


    @method_decorator(login_required(login_url='Main:loginapp'))
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


def delete_client(request,client_id):

    form = get_object_or_404(Client, id=client_id)
    form.delete()
    messages.success(request, "Formulaire Supprimer avec success!")
    return HttpResponseRedirect('/client')

def delete_substence(request,substence_id):

    form = get_object_or_404(Substence, id=substence_id)
    form.delete()
    messages.success(request, "Formulaire Supprimer avec success!")
    return HttpResponseRedirect('/substence')

def do_login(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        user=EmailBackend.authenticate(request,username=request.POST.get("email"),password=request.POST.get("password"))
        if user!=None:
            login(request,user)
            if user.user_type=='1':
                return HttpResponseRedirect("/admin")
            elif user.user_type=='2':
                return HttpResponseRedirect("/")
            else:
                messages.error(request,"Access Refusé. Merci de Reéssayer!!!")
                return HttpResponseRedirect(reverse('Main:loginapp'))

        else:
            messages.error(request,"Email ou mot de passe invalide")
            return HttpResponseRedirect(reverse('Main:loginapp'))



def logout_user(request):
    if request.user != None:
        logout(request)
    return redirect("/loginapp")
