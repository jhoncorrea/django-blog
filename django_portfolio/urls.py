"""
URL configuration for django_portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
#el include es para que incluye rutas de otras carpetas
from django.urls import path, include
#para las rutas de las imagenes
from django.conf.urls.static import static 
from django.conf import settings


#importo las vistas de la carpeta correspondiente
from portfolio import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    #importo de la carpeta blog el archivo url 
    path('blog/', include('blog.urls'))
]

#para la ruta de las imagenes
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)