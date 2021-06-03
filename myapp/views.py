from .models import Kontinent, Drzava, Lokacija
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required


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
    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # loging in
            user = form.get_user()
            login(request, user)
            return redirect('homepage')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    if request.method == 'GET':
        logout(request)
        return redirect('homepage')


@login_required(login_url="/login/")
def drzave_view(request, nazivKontinenta):
    kontinent = Kontinent.objects.get(naziv=nazivKontinenta)
    idKontinenta = kontinent.id
    drzave = Drzava.objects.filter(kontinentId=idKontinenta)
    return render(request, 'drzave.html', {'drzave': drzave})


@login_required(login_url="/login/")
def lokacije_view(request, nazivDrzave):
    drzava = Drzava.objects.get(naziv=nazivDrzave)
    idDrzave = drzava.id
    lokacije = Lokacija.objects.filter(drzavaId=idDrzave)
    return render(request, 'lokacije.html', {'lokacije': lokacije})


@login_required(login_url="/login/")
def lokacija_view(request, nazivLokacije):
    lokacija = Lokacija.objects.get(naziv=nazivLokacije)
    return render(request, 'lokacija.html', {'lokacija': lokacija})
