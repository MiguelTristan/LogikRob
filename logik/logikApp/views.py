from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# Acceso restringido
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from registration.models import Profile


# Create your views here.
def inicio(request):
    return render(request, 'logikApp/inicio.html')

def acerca(request):
    return render(request, 'logikApp/acerca.html')

def portfolio(request):
    count = User.objects.count()
    return render(request, 'logikApp/portafolio.html', {'contador':count})

@login_required
def aprende(request):
    profiles_v = Profile.objects.all()
    user_v = User.objects.all()
    return render(request, 'logikApp/aprende.html', {'perfiles_p':profiles_v, 'user_p':user_v})
