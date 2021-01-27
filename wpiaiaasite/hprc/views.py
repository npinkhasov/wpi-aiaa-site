from django.shortcuts import render

def index(request):
    context = {'nbar': 'home'}
    return render(request, "hprc/index.html", context)
