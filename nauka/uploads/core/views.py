from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from scipy import stats
from .forms import sprawdz


import csv
import pandas as pd


def glowna(request):
    print('Strona główna')
    return render(request, 'glowna.html')


def about(request):
    print('About')
    return render(request, 'about.html')


def contact(request):
    print('Contact')
    return render(request, 'contact.html')

def podstawy(request):
    print('Podstawy')
    return render(request, 'lekcje/podstawy.html' , {'podstawy':podstawy})

def ins_warun(request):
    print('Instrukcje warunkowe')
    return render(request, 'lekcje/ins_warun.html', {'ins_warun': ins_warun})

def petle(request):
    print('Pętle')
    return render(request, 'lekcje/petle.html', {'petle':petle})

def pseudolos(request):
    print('Liczby pseudolosowe')
    return render(request, 'lekcje/pseudolos.html', {'pseudolos':pseudolos})

def listy(request):
    print('Listy')
    return render(request, 'lekcje/listy.html', {'listy':listy})

def slowniki(request):
    print('Listy')
    return render(request, 'lekcje/slowniki.html', {'slowniki':slowniki})

def lancuch(request):
    print('Łańcuchy znaków')
    return render(request, 'lekcje/lancuch.html', {'lancuch':lancuch})

def funkcje(request):
    print('Funkcje')
    return render(request, 'lekcje/funkcje.html', {'funkcje':funkcje})

def klasy(request):
    print('Klasy')
    return render(request, 'lekcje/klasy.html', {'klasy':klasy})

import subprocess

def check(request):
  if request.method == 'GET':
    form = sprawdz()
  else:
    form = sprawdz()
    if form.is_valid():
      info = request.POST['info_name']
      output = script_function(info)
      ## Here you are calling script_function,
      ## passing the POST data for 'info' to it;
      return render(request, 'lekcje/check.html', {
        'info': info,
        'output': output,
      })
  return render(request, 'lekcje/check.html', {
    'form': form,
  })

def script_function( post_from_form ):
  print (post_from_form) ##optional,check what the function received from the submit;
  return subprocess.check_output(['/path/to/your/script.py', post_from_form])
