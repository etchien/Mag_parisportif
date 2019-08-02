"""DjangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib.auth.views import LoginView
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home ,name='home' ),
    path('register',views.register,name='register'),
    path('connexion',views.connexion, name='connexion'),
    path('profil',views.profil ,name='profil'),
    path('myLogin',LoginView.as_view(template_name="pages/connexion.html"),name='mylog'),
    path('mylogout',views.mylogout,name='mylogout'),
    path('resultat',views.resultat,name='resultat'),
     path('scrap',views.scrap,name='scrap'),

]
