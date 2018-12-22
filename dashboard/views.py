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
    print(conso_euro)
    cursor.execute("SELECT * FROM dashboard_conso_watt WHERE client_id = ?",(client_id,))
    conso_watt = cursor.fetchall()
    conso_euro_2016 = conso_euro[0]
    conso_euro_2017 = conso_euro[1]






    context = {
        "conso_euro": conso_euro,
        "conso_watt": conso_watt,
        "annual_costs": annual_costs,
        "is_elec_heating": is_elec_heating,
        "dysfunction_detected": dysfunction_detected
    }
    return render(request, 'dashboard/results.html', context)