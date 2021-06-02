from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Kontinent(models.Model):
    naziv = models.CharField(max_length=30, unique=True)

class Drzava(models.Model):
    naziv = models.CharField(max_length=30, unique=True)
    kontinentId = models.ForeignKey('Kontinent', on_delete=models.CASCADE)
    slika = models.ImageField(upload_to='static/drzave', default='static/img/bosna.jpg')
    brojLokacija = models.IntegerField(default=0)

class Lokacija(models.Model):
    naziv = models.CharField(max_length=30, unique=True)
    grad = models.CharField(max_length=30, default="")
    opis = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    glavna_slika = models.ImageField(upload_to='static/lokacije', default='static/img/travel.jpg')
    slika1 = models.ImageField(upload_to='static/lokacije', default='static/img/travel.jpg')
    slika2 = models.ImageField(upload_to='static/lokacije', default='static/img/travel.jpg')
    slika3 = models.ImageField(upload_to='static/lokacije', default='static/img/travel.jpg')
    slika4 = models.ImageField(upload_to='static/lokacije', default='static/img/travel.jpg')
    slika5 = models.ImageField(upload_to='static/lokacije', default='static/img/travel.jpg')
    slika6 = models.ImageField(upload_to='static/lokacije', default='static/img/travel.jpg')
    slika7 = models.ImageField(upload_to='static/lokacije', default='static/img/travel.jpg')
    slika8 = models.ImageField(upload_to='static/lokacije', default='static/img/travel.jpg')
    drzavaId = models.ForeignKey('Drzava', on_delete=models.CASCADE)

class Korisnik(models.Model):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=30)

class Ocjena(models.Model):
    vrijednost = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    korisnikId = models.ForeignKey('Korisnik', on_delete=models.CASCADE)
    lokacijaId = models.ForeignKey('Lokacija', on_delete=models.CASCADE)

class Recenzija(models.Model):
    tekst = models.TextField()
    korisnikId = models.ForeignKey('Korisnik', on_delete=models.CASCADE)
    lokacijaId = models.ForeignKey('Lokacija', on_delete=models.CASCADE)