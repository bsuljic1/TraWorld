from .models import Kontinent, Drzava
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout


def homepage(request):
    kontinenti = Kontinent.objects.all().order_by('naziv')
    return render(request, 'homepage.html', {'kontinenti': kontinenti})



def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # loging in
            user = form.save()
            login(request, user)
            return redirect('homepage')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', { 'form': form })


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #loging in
            user = form.get_user()
            login(request, user)
            return redirect('homepage')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', { 'form': form })

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('homepage')

def drzave_view(request, nazivKontinenta):
    kontinent = Kontinent.objects.get(naziv=nazivKontinenta)
    idKontinenta = kontinent.id
    drzave = Drzava.objects.filter(kontinentId=idKontinenta)
    return render(request, 'drzave.html', {'drzave': drzave})

