from django.shortcuts import render ,redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from  django.contrib.auth import  authenticate ,login ,logout
from .models import *

# Create your views here.
from django.http import JsonResponse
import json
from django.http import HttpResponse
from requests import get
from bs4 import BeautifulSoup


def scrap(request):
   url = 'https://www.matchendirect.fr/'
   response = get(url)
   html_soup = BeautifulSoup(response.text, 'html.parser')

   table = html_soup.find('div', attrs={'id': 'livescore'})
   compt = 1

   mydata = []

   for row in table.findAll('div', attrs={'class': 'panel panel-info'}):

      a_desc = row.find('h3', attrs={'class': 'panel-title'}).get_text()

      for el in row.findAll('tr'):
         resultat = {}
         heure = el.find('td', attrs={'class': 'lm1'}).get_text()
         eqA = el.find('span', attrs={'class': 'lm3_eq1'}).get_text()
         eqB = el.find('span', attrs={'class': 'lm3_eq2'}).get_text()

         scors = el.find('span', attrs={'class': 'lm3_score'}).get_text()

         resultat['heure'] = heure
         resultat['eqa'] = eqA
         resultat['eqb'] = eqB
         resultat['scors'] = scors

         mydata.append(resultat)

   data = mydata

   return JsonResponse(data, safe=False)

def resultat(request):
    url = 'https://www.matchendirect.fr/'
    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')

    table = html_soup.find('div', attrs={'id': 'livescore'})
    compt = 1

    mydata = []

    for row in table.findAll('div', attrs={'class': 'panel panel-info'}):

      a_desc = row.find('h3', attrs={'class': 'panel-title'}).get_text()

      for el in row.findAll('tr'):
         resultat = {}
         heure = el.find('td', attrs={'class': 'lm1'}).get_text()
         eqA = el.find('span', attrs={'class': 'lm3_eq1'}).get_text()
         eqB = el.find('span', attrs={'class': 'lm3_eq2'}).get_text()
         scors = el.find('span', attrs={'class': 'lm3_score'}).get_text()

         resultat['heure'] = heure
         resultat['eqa'] = eqA
         resultat['eqb'] = eqB
         resultat['scors'] = scors

         mydata.append(resultat)

      data = mydata
      send = {'resultat': data
      }
      print(send)

      return  render(request,'pages/resultat.html',send)



def home (request)       :
    return render(request,'pages/index.html')

def actualite(request)  :
  return render(request,'pages/actualite.html')

def register(request):

  if request.POST:
      userF = UserCreationForm(request.POST)
      if userF.is_valid():
          user = userF.save()
          user.save()
          return redirect('connexion')
  else:
      userF = UserCreationForm()
  return render(request, 'pages/inscription.html', {'f': userF})

  #   userName=request.POST.get('username' ,False)

  #   password=request.POST.get('password',False)

  #   try:

  #       user=User(username=userName)
  #       user.save()
  #       user.password=password
  #       user.set_password(user.password)
  #       user.save()
  #       print(userName,password)
  #       return redirect('mylog')

  #   except:

  #       print("Error get User or pasword")




def connexion(request):
    return render(request,'pages/connexion.html')

@login_required(login_url='mylog')
def profil(request):
    return render(request,'pages/profil.html')


def myLogin(request):
    return render('pages/conexion.html')
    # userName = request.POST['username']
    #
    # password = request.POST['password']
    #
    # user=authenticate(username=userName,password=password)
    #
    # if user is not None:
    #
    #     login(request,user)
    #
    #     return redirect('profil')
    # else:
    #     return redirect('mylog')

def mylogout(request):

    logout(request)

    return redirect('home')





