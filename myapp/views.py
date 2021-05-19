from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from .models import Kontinent

def homepage(request):
    kontinenti = Kontinent.objects.all().order_by('naziv')
    return render(request, 'index.html', {'kontinenti': kontinenti})