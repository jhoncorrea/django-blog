from django.contrib import admin
#primero importo el modelo
from .models import Project

# Register your models here.
admin.site.register(Project)