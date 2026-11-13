from django.shortcuts import render

def domace(request):
    return render(request, "domace/domace.html", {"domace_text": "Moje domace ulohy"})

def du2_vizitka(request):
    kontext = {
        "meno":"Bruno Vojtek",
        "trieda":"3.AT",
        "vek":17,
        "predmety":["Programovanie","Prax", "IoT"]
    }
    return render(request,'domace/du2_vizitka.html',{"kontext":kontext})
def du3_teplota(request):
    vysledok = None
    operacia = None
    if request.method == "POST":
        teplota = int(request.POST["teplota"])
        operacia = request.POST["operacia"]
        if operacia=="CF":
            vysledok = teplota*9/5+32
        elif operacia=="FC":
            vysledok = (teplota-32)*5/9
        vysledok = round(vysledok, 1)
    return render(request,'domace/du3_teplota.html',{'vysledok':vysledok,'operacia':operacia})
