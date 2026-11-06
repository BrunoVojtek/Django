from django.shortcuts import render, HttpResponse

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