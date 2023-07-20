from django.shortcuts import render
#importo de la carpeta .models
from .models import Project

# Create your views here.
def home(request):
    projects = Project.objects.all()
    return render(request, 'home.html', {
        'projects': projects
    })