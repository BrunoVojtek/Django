from django.shortcuts import render, HttpResponse
from datetime import datetime

def ahoj(request):
    return HttpResponse("Ahoj svet")
def o_mne(request):
    kontext ={
        "meno":"Bruno",
        "vek":17,
        "zaluby":["hasici","programovanie","3D print"]
    }
    return render(request,"ulohy/o_mne.html",kontext)
def rozvrh(request):
    hodiny=[
        {"cislo":1,"predmet":"Programovanie"},
        {"cislo":2,"predmet":"Programovanie"},
        {"cislo":3,"predmet":"Programovanie"},
        {"cislo":4,"predmet":"IoT"},
        {"cislo":5,"predmet":"IoT"},
        {"cislo":6,"predmet":"Anglicky jazyk"},
        {"cislo":7,"predmet":"Telesna vychova"}
    ]
    return render (request,'ulohy/rozvrh.html', {"den":"Piatok","hodiny":hodiny})
def pozdrav(request):
    meno = request.GET.get("meno","") # .get najde a vrati hodnotu prvku s indexom (klucom) meno ak ho nenajde vlozi ""
    return render(request, 'ulohy/pozdrav.html',{"meno":meno})
def sucet(request):
    vysledok = None
    if request.method == "POST":
        a = int(request.POST["a"])
        b = int(request.POST["b"])
        vysledok = a + b
    return render(request,'ulohy/sucet.html',{"vysledok":vysledok})
def kalkulacka(request):
    vysledok = None
    if request.method == "POST":
        a = float(request.POST["a"])
        b = float(request.POST["b"])
        znamienko = request.POST["znamienko"]
        if znamienko =="+":
            vysledok = a+b
        elif znamienko =="-":
            vysledok = a-b
        elif znamienko =="*":
            vysledok = a*b
        elif znamienko =="/":
            if b!=0:
                vysledok = a/b
            else:
                vysledok = "Nulou sa delit neda"
    return render(request,'ulohy/kalkulacka.html',{"vysledok":vysledok})
def obdlznik(request):
    obvod = None
    obsah = None
    if request.method =="POST":
        a = float(request.POST["a"])
        b = float(request.POST["b"])
        obvod = (a+b)*2
        obsah = a*b
        obvod=round(obvod,2)
        obsah=round(obsah,2)
    return render(request,'ulohy/obdlznik.html',{"obvod":obvod,"obsah":obsah})
def vek(request):
    aktualny_rok = datetime.now().year
    vek = None
    if request.method == "POST":
        vek = aktualny_rok - int(request.POST["rok"])
    return render(request,'ulohy/vek.html', {"vek":vek}) 