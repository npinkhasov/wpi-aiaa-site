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

def construction(request):
    context = {'nbar': 'dog'}
    return render(request, "hprc/construction.html", context)
    
def team(request):
    context = {'nbar': 'team'}
    return render(request, "hprc/team.html", context)
    
