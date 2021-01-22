from django.shortcuts import render
from .models import *


# Create your views here.

def home(request):
    projects = Project.objects.all()
    profile  = Profile.objects.order_by("-id")[0]
    context = {'projects': projects,'profile':profile}
    return render(request, 'portfolio/home.html', context)
