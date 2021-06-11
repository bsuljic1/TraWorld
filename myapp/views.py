from .models import Kontinent, Drzava, Lokacija, Recenzija
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage

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
    if request.method == 'POST':
            recenzija = Recenzija()
            recenzija.tekst = request.POST.get('review')
            recenzija.ocjena = request.POST.get('rating')
            recenzija.korisnik = request.user
            recenzija.lokacijaId = lokacija
            recenzija.save()
            return redirect('lokacija', nazivLokacije=nazivLokacije)

    ocjene = Recenzija.objects.filter(lokacijaId=lokacija.id)
    brojOcjena = ocjene.all().__len__()

    ocjena = 0
    for o in ocjene:
        ocjena = ocjena + o.ocjena
    ocjena = ocjena / (brojOcjena)

    ocjena5 = ocjene.filter(ocjena=5).all().__len__()
    ocjena4 = ocjene.filter(ocjena=4).all().__len__()
    ocjena3 = ocjene.filter(ocjena=3).all().__len__()
    ocjena2 = ocjene.filter(ocjena=2).all().__len__()
    ocjena1 = ocjene.filter(ocjena=1).all().__len__()

    ocjena5_bar = (ocjena5 / brojOcjena) * 100
    ocjena4_bar = (ocjena4 / brojOcjena) * 100
    ocjena3_bar = (ocjena3 / brojOcjena) * 100
    ocjena2_bar = (ocjena2 / brojOcjena) * 100
    ocjena1_bar = (ocjena1 / brojOcjena) * 100

    recenzije1 = ocjene.all()
    p = Paginator(recenzije1, 3)
    page_num = request.GET.get('page', 1)

    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)


    return render(request, 'lokacija.html', {'lokacija': lokacija, 'ocjena': ocjena, 'brojOcjena': brojOcjena,
                                             'recenzije': page, 'ocjena5': ocjena5, 'ocjena4': ocjena4,
                                             'ocjena3': ocjena3, 'ocjena2': ocjena2, 'ocjena1': ocjena1,
                                             'ocjena5_bar': ocjena5_bar, 'ocjena4_bar': ocjena4_bar, 'ocjena3_bar': ocjena3_bar,
                                             'ocjena2_bar': ocjena2_bar, 'ocjena1_bar': ocjena1_bar})


# def create_review(request):
#     if request.method == 'POST':
#         if request.POST.get('title') and request.POST.get('content'):
#             recenzija = Recenzija()
#             recenzija.tekst = request.POST.get('review')
#             recenzija.korisnik = request.user
#             recenzija.lokacijaId = request.
#             recenzija.save()
#             return render(request, 'posts/create.html')
#
#         else:
#             return render(request, 'posts/create.html')
#
#     return render(request, 'signup.html', {'form': form})
