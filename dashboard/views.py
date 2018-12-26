# coding: utf-8
from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import ClientForm
from .models import Conso_eur, Conso_watt
import sqlite3

class ClientFormView(View):
    def get(self, request):
        return render(request, 'dashboard/accueil.html')

    def post(self, request):
        form = ClientForm(request.POST)

        if form.is_valid():
            client_id = form.cleaned_data['client']
            return redirect('dashboard:results', client_id=client_id)

def results(request, client_id):
    conso_euro = []
    conso_watt = []
    annual_costs = [0, 0]
    is_elec_heating = True
    dysfunction_detected = False


    ###################################
    # ----> YOUR CODE GOES HERE <---- #
    ###################################

    #On commence par se connecter à la base de donnée
    con = sqlite3.connect('db.sqlite3')
    #On va affecter les conso en euro et en watt aux variables conso_watt et conso_eur
    cursor = con.cursor()
    cursor.execute("SELECT * FROM dashboard_conso_eur WHERE client_id = ?",(client_id,))
    conso_euro = cursor.fetchall()
    #On va séparer les deux consommations annuelles
    conso_euro_2016 = conso_euro[0]
    conso_euro_2016 = list(conso_euro_2016)
    #On va garder uniquement les valeurs des consommations des mois dans la liste
    del conso_euro_2016[0]
    del conso_euro_2016[len(conso_euro_2016)-1]
    del conso_euro_2016[len(conso_euro_2016)-1]
    conso_euro_2017 = conso_euro[1]
    conso_euro_2017 = list(conso_euro_2017)
    del conso_euro_2017[0]
    del conso_euro_2017[len(conso_euro_2017)-1]
    del conso_euro_2017[len(conso_euro_2017)-1]
    #On va sommer les consommations pour obtenir les dépenses annuelles. on arrondit le résultat à 2 décimales
    annual_costs=[round(sum(conso_euro_2016),2),round(sum(conso_euro_2017),2)]


    cursor.execute("SELECT * FROM dashboard_conso_watt WHERE client_id = ?",(client_id,))
    conso_watt = cursor.fetchall()
    conso_watt_2017 = conso_watt[1]
    conso_watt_2017 = list(conso_watt_2017)
    del conso_watt_2017[0]
    del conso_watt_2017[len(conso_watt_2017)-1]
    del conso_watt_2017[len(conso_watt_2017)-1]

    #Chauffage électrique
    #Pour déterminer si l'utilsateur possède un chauffage électrique, on va regarder sa consommation en hiver.
    #On regarde si parmi les mois de Novembre,Décembre,Janvier,Février (Hiver), 3 de ces mois correspondent
    #Aux consommations les plus élevés de l'année.

    #Il est tout à fait possible de redéfinir le critère permettant de savoir si l'utilisateur possède un chauffage électrique ou non

    #On travaille sur l'année la plus récente, à savoir 2017.

    Novembre = conso_watt_2017[4]
    Decembre = conso_watt_2017[5]
    Janvier = conso_watt_2017[6]
    Fevrier = conso_watt_2017[7]
    i=0

    conso_watt_2017_copy = list(conso_watt_2017)
    del conso_watt_2017_copy[4]
    del conso_watt_2017_copy[4]
    del conso_watt_2017_copy[4]
    del conso_watt_2017_copy[4]

    if Novembre >= max(conso_watt_2017_copy):
        i=i+1
    if Decembre >= max(conso_watt_2017_copy):
        i=i+1
    if Janvier >= max(conso_watt_2017_copy):
        i=i+1
    if Fevrier >= max(conso_watt_2017_copy):
        i=i+1
    if i<3:
        is_elec_heating = False


    #Dysfonctionnement
    #Pour déterminer un dysfonctionnement, on regarde si la consomation entre 2016 n'a pas trop varié.
    #On va fixer un seuil de 25% pour avoir un critère de dysfonctionnement.
    #Cela est valable lors d'une hausse, comme d'une baisse.

    a=min(annual_costs)
    pourcentage=abs(annual_costs[0]-annual_costs[1])
    print(pourcentage)
    pourcentage=pourcentage/float(a)
    pourcentage=pourcentage*100
    pourcentage=round(pourcentage,2)

    if pourcentage >= 25:
        dysfunction_detected = True






    context = {
        "conso_euro": conso_euro,
        "conso_euro_2016":conso_euro_2016,
        "conso_euro_2016_juillet": conso_euro_2016[0],
        "conso_euro_2016_aout": conso_euro_2016[1],
        "conso_euro_2016_septembre": conso_euro_2016[2],
        "conso_euro_2016_octobre": conso_euro_2016[3],
        "conso_euro_2016_novembre": conso_euro_2016[4],
        "conso_euro_2016_decembre": conso_euro_2016[5],
        "conso_euro_2016_janvier": conso_euro_2016[6],
        "conso_euro_2016_fevrier": conso_euro_2016[7],
        "conso_euro_2016_mars": conso_euro_2016[8],
        "conso_euro_2016_avril": conso_euro_2016[9],
        "conso_euro_2016_mai": conso_euro_2016[10],
        "conso_euro_2016_juin": conso_euro_2016[11],

        "conso_euro_2017":conso_euro_2017,
        "conso_euro_2017_juillet": round(conso_euro_2017[0],2),
        "conso_euro_2017_aout": round(conso_euro_2017[1],2),
        "conso_euro_2017_septembre": round(conso_euro_2017[2],2),
        "conso_euro_2017_octobre": round(conso_euro_2017[3],2),
        "conso_euro_2017_novembre": round(conso_euro_2017[4],2),
        "conso_euro_2017_decembre": round(conso_euro_2017[5],2),
        "conso_euro_2017_janvier": round(conso_euro_2017[6],2),
        "conso_euro_2017_fevrier": round(conso_euro_2017[7],2),
        "conso_euro_2017_mars": round(conso_euro_2017[8],2),
        "conso_euro_2017_avril": round(conso_euro_2017[9],2),
        "conso_euro_2017_mai": round(conso_euro_2017[10],2),
        "conso_euro_2017_juin": round(conso_euro_2017[11],2),

        "conso_watt": conso_watt,
        "conso_watt_2017":conso_watt_2017,
        "conso_watt_2017_juillet": conso_watt_2017[0],
        "conso_watt_2017_aout": conso_watt_2017[1],
        "conso_watt_2017_septembre": conso_watt_2017[2],
        "conso_watt_2017_octobre": conso_watt_2017[3],
        "conso_watt_2017_novembre": conso_watt_2017[4],
        "conso_watt_2017_decembre": conso_watt_2017[5],
        "conso_watt_2017_janvier": conso_watt_2017[6],
        "conso_watt_2017_fevrier": conso_watt_2017[7],
        "conso_watt_2017_mars": conso_watt_2017[8],
        "conso_watt_2017_avril": conso_watt_2017[9],
        "conso_watt_2017_mai": conso_watt_2017[10],
        "conso_watt_2017_juin": conso_watt_2017[11],

        "annual_costs": annual_costs,
        "Depense_2016": annual_costs[0],
        "Depense_2017": annual_costs[1],

        "is_elec_heating": is_elec_heating,

        "dysfunction_detected": dysfunction_detected,
        "pourcentage":pourcentage,
    }
    return render(request, 'dashboard/results.html', context)