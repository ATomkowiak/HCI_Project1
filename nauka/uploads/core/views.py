from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from scipy import stats

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

def data_analysis(request):
    print('Data analysis')
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']

        print('\nWhat is `myfile`?')
        print(type(myfile))

        print('\nDirectly accessing `myfile` gives nothing :(')
        print(type(str(myfile.read())))
        print(str(myfile.read()))

        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        print('\nHowever, when using FileSystemStorage...')
        print('\nReading filename: %s' % filename)
        print(type(fs.open(filename)))
        print(fs.open(filename))

        print('\nOpen and preview using pandas:')
        df = pd.read_csv(fs.open(filename))
        print(df)

        print('\nOr with CSV module:')
        with fs.open(filename, 'rt') as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            for row in readCSV:
                print(row)

        print('Data analysis')
        r_table = df.apply(lambda x: df.apply(lambda y: r_xor_p(x, y,
                                                                r_xor_p='r')))
        p_table = df.apply(lambda x: df.apply(lambda y: r_xor_p(x, y,
                                                                r_xor_p='p')))

        return render(request, 'data_analysis.html',
                      {'result_present': True,
                       'results': {'r_table': r_table.to_html(),
                                   'p_table': p_table.to_html()},
                       'df': df.to_html()})

    return render(request, 'data_analysis.html')


def r_xor_p(x, y, r_xor_p='r'):
    ''' Pearson's r or its p
    Depending of what you would like to get.
    '''
    r, p = stats.pearsonr(x, y)

    if r_xor_p == 'r':
        return r
    else:
        return p
