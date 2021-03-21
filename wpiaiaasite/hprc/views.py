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
        "year": "2018-2019",
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
        },
        "image": 'hprc/img/officers/rocketlead.jpg',
        "text": [
            "Our first Launch Vehicle named Batman, was designed to reach an apogee of approximately 4094 ft on the motor picked for launch. The Launch Vehicle split into four main sections over the course of its decent and each tethered section was designed to have a GPS, totaling 3 GPS devices. Upon full separation, the sections were defined as the upper airframe, the lower airframe, the payload retention system, which are all tethered together, and the nose cone. Housed within the upper airframe was the payload retention system made of airframe tubing dedicated to housing the selected payload for the duration of its flight. The vehicle had three parachutes, a nose cone parachute, drogue parachute and main parachute. The launch vehicle’s flight data was recorded using a Raven 3 Altimeter that was housed in the electronics bay.",
            "Our selected design for our payload, named Robin, was a quadrotor UAV housed within a cylindrical retention system composed of Blue Tube. The tube held the UAV as well as a 3D printed base to hold the UAV in place and was to be ejected from the rocket during descent. When activated, the system was designed to unfold, opening its four arms to right itself in the process to deploy the UAV. This unfolding design allowed for a very simplistic and reliable system, containing few moving parts to minimize points of failure as well as being highly spatially efficient.",
            
        ]
    }
    return render(request, "hprc/project.html", context)