from django.shortcuts import render
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from AppPrincipal.forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

@login_required
def observation(request):
    template = loader.get_template('observations.html')  # Get the template
    context = {}
    return HttpResponse(template.render(context, request))  # Render the template with the context
def connexion(request):
    if request.method == 'POST':
        username = request.POST['identifiant']
        password = request.POST['pass1']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('observation')
        else :
            render(request,'registration/login.html')

    return render(request,'registration/login.html')
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm()
        if form.is_valid:
            uname = request.POST.get('identifiant')
            pass1 = request.POST.get('pass1')
            pass2 = request.POST.get('pass2')

            visiteur = User.objects.create_user(username=uname, password=pass1)
            visiteur.save()
            return redirect('/connexion/')
    else:
        form = UserCreationForm()
    return render(request,'registration/signup.html',{'form':form})

# Create your views here.
def index(request):
    page = loader.get_template('base.html')
    context = {
        'title': 'Home',
    }
    return HttpResponse(page.render(context,request))

def skills(request):
    page = loader.get_template('skills.html')
    context = {
        'title': 'Skill',
    }
    return HttpResponse(page.render(context,request))

def resume(request):
    page = loader.get_template('parcours.html')
    context = {
        'title': 'Parcours',
    }
    return HttpResponse(page.render(context,request))

def realisation(request):
    page = loader.get_template('realisation.html')
    context = {
        'title': 'Réalisation',
    }
    return HttpResponse(page.render(context,request))

def loisir(request):
    page = loader.get_template('loisirs.html')
    context = {
        'title': 'Loisirs',
    }
    return HttpResponse(page.render(context,request))

def contact(request):
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            nom = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            message = form.cleaned_data.get('message')
            try:
                 send_mail(nom, message, email, ["marc.ravoahangy@outlook.fr"])
                
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return redirect('/contact/')
    return render(request, "contact.html", {"form": form})