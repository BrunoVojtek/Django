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
