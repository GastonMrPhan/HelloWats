// ----> YOUR CODE HERE <----


//Tableau des dépenses
//On commence par cacher les détails

$('.mois2017').hide();
$('.depenses2017').hide();

$('.mois2016').hide();
$('.depenses2016').hide();

//Affichage des détails lorsqu'on appuie sur les boutons détails

$('#Bouton2017').click(function(){
  $('.mois2017').fadeToggle();
  $('.depenses2017').fadeToggle();

});

$('#Bouton2016').click(function(){
  $('.mois2016').fadeToggle();
  $('.depenses2016').fadeToggle();

});

//Consommation 2017
//On définit les variables à mettre en ordonnées
var conso_watt_2017_juillet = document.getElementById("conso_watt_2017_juillet").value;
var conso_watt_2017_aout = document.getElementById("conso_watt_2017_aout").value;
var conso_watt_2017_septembre = document.getElementById("conso_watt_2017_septembre").value;
var conso_watt_2017_octobre = document.getElementById("conso_watt_2017_octobre").value;
var conso_watt_2017_novembre = document.getElementById("conso_watt_2017_novembre").value;
var conso_watt_2017_decembre = document.getElementById("conso_watt_2017_decembre").value;
var conso_watt_2017_janvier = document.getElementById("conso_watt_2017_janvier").value;
var conso_watt_2017_fevrier = document.getElementById("conso_watt_2017_fevrier").value;
var conso_watt_2017_mars = document.getElementById("conso_watt_2017_mars").value;
var conso_watt_2017_avril = document.getElementById("conso_watt_2017_avril").value;
var conso_watt_2017_mai = document.getElementById("conso_watt_2017_mai").value;
var conso_watt_2017_juin = document.getElementById("conso_watt_2017_juin").value;



var data = [
      { y: 'Juillet', a: conso_watt_2017_juillet, b: 90},
      { y: 'Aout', a: conso_watt_2017_aout ,  b: 75},
      { y: 'Septembre', a: conso_watt_2017_septembre,  b: 50},
      { y: 'Octobre', a: conso_watt_2017_octobre,  b: 60},
      { y: 'Novembre', a: conso_watt_2017_novembre,  b: 65},
      { y: 'Décembre', a: conso_watt_2017_decembre,  b: 70},
      { y: 'Janvier', a: conso_watt_2017_janvier, b: 75},
      { y: 'Février', a: conso_watt_2017_fevrier, b: 75},
      { y: 'Mars', a: conso_watt_2017_mars, b: 85},
      { y: 'Avril', a: conso_watt_2017_avril, b: 85},
      { y: 'Mai', a: conso_watt_2017_mai, b: 95},
      { y: 'Juin', a: conso_watt_2017_juin, b: 95},
    ],
    //On précise les configurations de notre bar chart
    config = {
      data: data,
      xkey: 'y',
      ykeys: ['a'],
      labels: ['Consommation',],
      fillOpacity: 0.6,
      hideHover: 'auto',
      barSizeRatio:0.5,
      behaveLikeLine: true,
      resize: true,
      pointFillColors:['#ffffff'],
      pointStrokeColors: ['black'],
      lineColors:['gray','red']
  };
config.element = 'bar-chart';
Morris.Bar(config);


//Chauffage électrique

var is_elec_heating = document.getElementById("is_elec_heating").value;


$('#Vrai').hide();
$('#Faux').hide();

function AffichageChauffage(){
    if (is_elec_heating == 'True') {
        $('#Vrai').show();
    }
    else{

        $('#Faux').show();
    }
};

AffichageChauffage();

//Dysfonctionnement
var dysfunction_detected = document.getElementById("dysfunction_detected").value;
$('.Dysfonctionnement').hide();

//On affiche le message de dysfonctionnement uniquement lorsqu'on en détecte un.
function AffichageAlerte(){
    if (dysfunction_detected == 'True'){
        $('.Dysfonctionnement').show();
    }

}
AffichageAlerte();