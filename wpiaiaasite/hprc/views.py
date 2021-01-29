from django.shortcuts import render


def index(request):
    context = {'nbar': 'home'}
    return render(request, "hprc/index.html", context)


def sponsors(request):
    context = {'nbar': 'sponsors'}
    return render(request, "hprc/sponsors.html", context)

def sponsorpackage(request):
    context = {'nbar': 'sponsors'}
    return render(request, "hprc/sponsorpackage.html", context)
