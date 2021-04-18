from django.db import models

class Kontinent(models.Model):
    naziv = models.CharField(max_length=30, unique=True)

class Drzava(models.Model):
    naziv = models.CharField(max_length=30, unique=True)
    kontinentId = models.ForeignKey('Kontinent', on_delete=models.CASCADE)

class Lokacija(models.Model):
    naziv = models.CharField(max_length=30, unique=True)
    opis = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    drzavaId = models.ForeignKey('Drzava', on_delete=models.CASCADE)

class Korisnik(models.Model):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=30)

class Ocjena(models.Model):
    vrijednost = models.IntegerField()
    korisnikId = models.ForeignKey('Korisnik', on_delete=models.CASCADE)
    lokacijaId = models.ForeignKey('Lokacija', on_delete=models.CASCADE)

class Recenzija(models.Model):
    tekst = models.TextField()
    korisnikId = models.ForeignKey('Korisnik', on_delete=models.CASCADE)
    lokacijaId = models.ForeignKey('Lokacija', on_delete=models.CASCADE)