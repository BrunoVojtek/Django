from django.shortcuts import render

def index(request):
    kontext= {
        "meno":"Bruno",
        "priezvisko":"Vojtek",
        "ulohy":["programovanie"]
    }
    return render(request,"domace/index.html",kontext)
