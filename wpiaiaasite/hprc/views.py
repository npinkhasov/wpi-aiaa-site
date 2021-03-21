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
    
def goats(request):
    context = {
        'nbar': "projects",
        "project_title": "G.O.A.T.S",
        "lead_text": "WPI's first year competing in USLI",
        "docs": {
            "Proposal": "link",
            "Preliminary Design Review": "link",
            "Comprehensive Design Review": "link",
            "Flight Readiness Review": "link",
            "Post-Launch Assessment Review": "link",
        },
        "sponsors": {
            "Platinum": [
                "Jones Machine Company"
            ],
            "Bronze": [
                "Test Devices Inc.",
                "Plasma Technology Inc.",
                "Consulting Structural Engineering Inc.",
            ]
        }
    }
    return render(request, "hprc/project.html", context)