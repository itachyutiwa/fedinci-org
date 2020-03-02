from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRegister,UserUpdate, ProfileUpdate
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Profile


# Create your views here.
@login_required(login_url='connexion')
def evenements(request):
    return render(request, 'evenements.html',{'title':'Evènements'})

@login_required(login_url='connexion')
def rendez_vous(request):
    return render(request, 'rendez_vous.html', {'title':'Rendez-vous'})

def contact(request):
    return render(request, 'contact.html',{'title':'Contactez-nous'})

def home(request):
    return render(request, 'index.html',{'title':'Bienvenue'})

@login_required(login_url='connexion')
def services(request):
    return render(request, 'services.html', {'title':'Services'})

def devenir_membre(request):
    return render(request, 'devenir_membre.html',{'title':'Inscription'})

def nos_institutions(request):
    return render(request, 'nos_institutions.html',{'title':'Institutions internes'})

@login_required(login_url='connexion')
def prix_et_laureats(request):
    return render(request, 'prix_et_laureats.html',{'title':'Prix inventeurs et lauréats'})

@login_required(login_url='connexion')
def protection(request):
    return render(request, 'protection.html', {'title':'Protection'})

def videos_et_medias(request):
    return render(request, 'videos_et_medias.html', {'title':'Vidéos et Médias'})

def a_propos_de_nous(request):
    return render(request, 'a_propos_de_nous.html', {'title':'A propos de nous'})

def inscription(request):
    if request.method == 'POST':
        form=UserRegister(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request, f'Félicitation, le compte de {username} a été crée avec succès. Connectez-vous maintenant!')
            return redirect('connexion')
    else:
        form=UserRegister()
    return render(request, 'inscription.html',{'title':'Inscription','form':form})

def connexion(request):
    if request.method == 'POST':
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                messages.success(request, f'Vous etes connecté en tant que {username}')
                return redirect('home') 
    else:
        form=AuthenticationForm()
    return render(request, 'connexion.html',{'title':'Connexion', 'form':form})

@login_required(login_url='connexion')
def profile(request):
    user, created = Profile.objects.get_or_create(user=request.user)
    user.is_active=True
    if request.method =='POST':
        u_form=UserUpdate(request.POST,instance=request.user)
        p_form=ProfileUpdate(request.POST ,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Votre profil a bien été mis à jour')
            return redirect('profile')
    else:
        u_form=UserUpdate(instance=request.user)
        p_form=ProfileUpdate(instance=request.user.profile)
    return render(request, 'profile.html',{'title':'Profil','u_form':u_form,'p_form':p_form})

def deconnexion(request):
    logout(request)
    messages.warning(request, f'Vous etes déconnecté, reconnectez-vous!')
    return redirect('connexion')

def tous_les_membres(request):
    tous_les_membres={
        'tous_les_membres':Profile.objects.all().order_by(),
        'title':'Tous les membres',
    }
    return render(request, 'tous_les_membres.html', tous_les_membres)

def member_detail(request, pk):
    unique_object=get_object_or_404(Profile, pk=pk)
    unique_object={
        'unique_object':unique_object
    }
    return render(request, 'member_detail.html', unique_object)