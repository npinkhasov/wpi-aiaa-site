from django.shortcuts import render

def index(request):
    context = {'nbar': 'home'}
    return render(request, "home/index.html", context)

def subcommittees(request):
    context = {'nbar': 'subcommittees'}
    return render(request, "home/subcommittees.html", context)

def events(request):
    context = {'nbar': 'events'}
    return render(request, "home/events.html", context)

def about(request):
    context = {'nbar': 'about'}
    return render(request, "home/about.html", context)

def proposal(request):
    context = {'nbar': 'subcommittees'}
    return render(request, "home/jetproposal.html", context)

def handler400(request, *args, **argv):
    context = {'nbar': request.path[1:]}
    response = render(request, "home/400.html", context)
    response.status_code = 400
    return response

def handler403(request, *args, **argv):
    context = {'nbar': request.path[1:]}
    response = render(request, "home/403.html", context)
    response.status_code = 403
    return response

def handler404(request, *args, **argv):
    context = {'nbar': request.path[1:]}
    response = render(request, "home/404.html", context)
    response.status_code = 404
    return response

def handler500(request, *args, **argv):
    context = {'nbar': request.path[1:]}
    response = render(request, "home/404.html", context)
    response.status_code = 500
    return response