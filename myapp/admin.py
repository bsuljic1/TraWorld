from django.contrib import admin
from .models import Kontinent, Drzava, Lokacija, Ocjena, Recenzija

# Register your models here.
admin.site.register(Kontinent)
admin.site.register(Drzava)
admin.site.register(Lokacija)
admin.site.register(Ocjena)
admin.site.register(Recenzija)
