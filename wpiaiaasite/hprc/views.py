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

def contact(request):
    context = {'nbar': 'contact'}
    return render(request, "hprc/contact.html", context)
    
def team(request):
    context = {'nbar': 'team'}
    return render(request, "hprc/team.html", context)
    
def sirius(request):
    context = {
        'nbar': "projects",
        "project_title": "Sirius and Polaris",
        "year": "2020-2021",
        "docs": {
            "Proposal": "hprc/sirius/WPI HPRC Proposal 2021.pdf",
            "Preliminary Design Review": "hprc/sirius/WPI HPRC PDR 2021.pdf",
            "Critical Design Review": "hprc/sirius/WPI HPRC CDR 2021.pdf",
            # "Flight Readiness Review": "hprc/goddard/Worcester Polytechnic Institute - 2020 - FRR Report.pdf",
        },
        # "photos": "https://photos.app.goo.gl/nweEEhFTJYfKczVr8",
        "sponsors": {
            "Gold": [
                "WPI Tinkerbox",
                "Ensign-Bickford Aerospace & Defense"
            ],
            "Bronze": [
                "Test Devices Inc.",
                "Consulting Structural Engineer Inc.",
                "HydroCutter"
            ]
        },
        "image": 'hprc/sirius/cnc.jpg',
        "caption": "A member prepares fixtures in a CNC mill before machining components for the motor retention.",
        "text": [
            (
                "Entering their third year, WPI USLI made the decision to rebrand to the High Power Rocketry Club (HPRC).  "
                "This year was uniquely challenging as the COVID-19 pandemic prevented the majority in person meetings.  "
                "While the team initially continued to compete in NASA Student Launch, the competition was dropped in December "
                "as there was no way for the team to fulfill launch requirements while staying in compliance with WPI's and the CDC's "
                "COVID safety guidelines.  Despite this, the team continued designing and building our rocket and payload.  There is "
                "still a lot to learn by flying the mission, even if it is not at the competition."
            ),
            (
                "The team's rocket, Sirius, continues to build upon the experience gained in the past two competition years. "
                "It contains many new systems such as forward mounted motor retention, an airbrake system, and a custom "
                "avionics board.  The vehicle has a predicted apogee of 4934 ft but has a target apogee of 4550 ft.  "
                "To ensure there is no overshoot, the airbrake system is actively controlled by the avionics to produce "
                "just enough drag to reduce the vehicle's apogee to the target."
            ),
            (
                "The vehicle's payload is a lander designated Polaris.  After being ejected from the vehicle during descent, Polaris "
                "lands under its own parachute before engaging its self-righting system which rights the payload from any "
                "orientation using a set of outward folding petals.  This is more finely adjusted by the stabilization system "
                "which uses a set of legs that deploy to level the payload within 5 degrees on uneven terrain.  Finally, "
                "it takes a panoramic photo using its top mounted camera before transmitting the photo back to a ground station."
            )
        ],
        "officers": {
            "Captain": "Kirsten Bowers",
            "Rocket Lead": "Troy Otter",
            "Payload Lead": "Thierry de Crespingy",
            "Safety Officer": "Michael Beskid",
            "Treasurer": "Kevin Schultz",
            "Logistics Officer": "Nikita Jagdish",
            "Sponsorship Officer": "Julia Sheats",
            "Documentation Officer": "Christian M. Schrader",
            "Outreach Officer": "Connor Walsh",
            "Public Relations Officer": "Christopher Davenport", 
        }
    }
    return render(request, "hprc/project.html", context)

def goddard(request):
    context = {
        'nbar': "projects",
        "project_title": "Project Goddard",
        "year": "2019-2020",
        "docs": {
            "Proposal": "hprc/goddard/Worcester Polytechnic Institute - 2020 - Proposal.pdf",
            "Preliminary Design Review": "hprc/goddard/Worcester Polytechnic Institute - 2020 - PDR Report.pdf",
            "Critical Design Review": "hprc/goddard/Worcester Polytechnic Institute - 2020 - CDR Report.pdf",
            "Flight Readiness Review": "hprc/goddard/Worcester Polytechnic Institute - 2020 - FRR Report.pdf",
        },
        "photos": "https://photos.app.goo.gl/nweEEhFTJYfKczVr8",
        "sponsors": {
            "Platinum": [
                "Jones Machine Company"
            ],
            "Bronze": [
                "Test Devices Inc.",
                "Plasma Technology Inc.",
                "Consulting Structural Engineer Inc.",
            ]
        },
        "image": 'hprc/goddard/testflight.jpg',
        "caption": "The team takes a group photo right before Phoenix takes flight over Lake Winnipesaukee.",
        "text": [
            (
                "Beginning the second year of the team, WPI USLI (HPRC's former team name) now had some experience.  "
                "With a better understanding of the competition, team organization was overhauled bringing new "
                "officer positions, more streamlined report writing, and an even larger team.  This year's project "
                "was designated Project Goddard, named after Robert Goddard, the father of modern rocketry and "
                "one of WPI's most famed alumni.  "
            ),
            (
                "The team's second launch vehicle, named Phoenix, measured 111 in long and was built out of 6 inch "
                "Blue Tube 2.0.  Flying on an L1050 solid rocket motor, it was projected to reach an apogee of 4088 ft.  "
                "The vehicle embodied the many lessons learned in the team's first year.  Gone was last year's heavy "
                "fin can, replaced with a light weight and 3D printed bracket set that held in " 
                "place a set of four custom made foam core carbon-fiber fins.  Last year's electronics bay, which took "
                "more than an hour of prep time at the launch site, was redone with a twist lock mechanism that could be "
                "assembled in minutes.  These and many other changes put the team's new knowledge to good use."
            ),
            (
                "The goal of the payload, named Icarus was to mechanically retain and deploy an Unmanned Aerial Vehicle "
                "(UAV) to collect a sample from a designated area. In order to perform this function, we "
                "designed a lead screw driven retention system which oriented and lifted the UAV out of the rocket body "
                "and an unfolding drone capable of collecting a 15ml soil sample.  Compared with last year's design, Icarus "
                "was easier to manufacture thanks to better material choices and performed well in test missions."
            ),
            (
                "Phoenix and Icarus flew one test flight from Lake Winnipesaukee in February.  Unfortunately, a manufacturing "
                "defect in the motor the team bought caused the vehicle to underperform and not reach the expected apogee.  "
                "Outside of that, the vehicle performed excellently and proved to require significantly less prep time at the "
                "launch site in order to fly.  "
                "While the team was excited to return to Huntsville with our new and improved rocket and payload, the competition "
                "was cancelled due to the outbreak of the COVID-19 pandemic.  Despite this, the team learned a lot, gained new "
                "sponsors, and became well prepared for future years."
            )
        ],
        "officers": {
            "Captain": "Christian M. Schrader",
            "Rocket Lead": "Sophie Balkind",
            "Payload Lead": "Thierry de Crespingy",
            "Safety Officer": "Veronika Karshina",
            "Treasurer": "Kirsten Bowers",
            "Logistics Officer": "Troy Otter",
            "Philanthropy Officer": "Adrianne Curtis",
            "Documentation Officer": "Jeremiah Valero",
            "Outreach Officer": "Connor Walsh",
            "Social Media Officer": "Christopher Renfro", 
        }
    }
    return render(request, "hprc/project.html", context)

def goats(request):
    context = {
        'nbar': "projects",
        "project_title": "G.O.A.T.S",
        "year": "2018-2019",
        "docs": {
            "Proposal": "hprc/goats/Worcester Polytechnic Institute - 2019 - Proposal.pdf",
            "Preliminary Design Review": "hprc/goats/Worcester Polytechnic Institute - 2019 - PDR Report.pdf",
            "Critical Design Review": "hprc/goats/Worcester Polytechnic Institute - 2019 - CDR Report.pdf",
            "Flight Readiness Review": "hprc/goats/Worcester Polytechnic Institute - 2019 - FRR Report.pdf",
            "Post-Launch Assessment Review": "hprc/goats/Worcester Polytechnic Institute - 2019 - PLAR Report.pdf",
        },
        "photos": "https://photos.app.goo.gl/kshVddRy9KsDYAGA6",
        "sponsors": {
            "Silver": [
                "Hydrocutter Inc.",
            ]
        },
        "image": 'hprc/goats/fair.jpg',
        "caption": "The team presenting their rocket and payload at the NASA SLI rocket fair.",
        "text": [
            (
                "While WPI had competed in rocketry competitions previously, namely Battle of the Rockets, "
                "HPRC as we know it today was first founded in 2018 as WPI University Student Launch Initiative (USLI). "
                "After pitching the project to the AIAA "
                "Officer Board, the team received its initial funding.  The project name, G.O.A.T.S was selected for WPI's "
                "mascot, Gompei the goat, in addition to the fact that we just like acronyms.  Having just started out, the members "
                "of the team lacked experience.  The officers were mostly sophomores leading a large "
                "group of mostly freshmen.  Despite this, the team spent the year learning and overcoming "
                "challenges at every step.  They submitted their first design reviews, solved unexpected "
                "vehicle packing problems at their subscale launch, and even rebuilt the entire lower airframe "
                "in a week after its loss due to bulkhead failure on its first test flight."
            ),
            (
                "While not every rookie team makes it to launch week, WPI got there, beating many tough challenges "
                "along the way.  Ultimately, when the team's rocket took flight at the competition launch in Huntsville, "
                "it was destroyed at around 800ft due to a defect in the motor the team purchased.  While it may have "
                "been disappointing, the team still returned home excited.  The members learned a lot from meeting with "
                "other teams and NASA engineers and were already brainstorming new ideas for next year before launch week "
                "was over.  The first year was not perfect, but it cemented the team as WPI's premier rocketry team."
            ),
            (
                "Our first launch vehicle named, Batman, was designed to reach an apogee of approximately " 
                "4094 ft on the motor picked for launch. The launch vehicle split into four independent sections "
                "over the course of its decent. Upon full separation, the sections were defined as the upper airframe, the lower "
                "airframe, the payload retention system, which are all tethered together, and the nose cone, which descended seperately. "
                "Housed within the upper airframe was the payload retention system made of airframe tubing "
                "dedicated to housing the selected payload for the duration of its flight. The vehicle had three "
                "parachutes, a nose cone parachute, drogue parachute and main parachute. The launch vehicle’s "
                "flight data was recorded using a Raven 3 Altimeter that was housed in the electronics bay."
            ),
            (
                "Our selected design for our payload, named Robin, was a quadrotor UAV housed within a cylindrical "
                "retention system composed of Blue Tube 2.0. The tube held the UAV as well as a 3D printed base to hold "
                "the UAV in place and was to be ejected from the rocket during descent. When activated, the system "
                "was designed to unfold, opening its four arms to right itself in the process to deploy the UAV. "
                "This unfolding design allowed for a very simple and reliable system, containing few moving parts "
                "to minimize points of failure while remaining spatially efficient."
            ),
        ],
        "officers": {
            "Captain": "Caroline Kuhnle",
            "Systems Integration/Rocket Lead": "Krystina Waters",
            "Safety Officer": "Christian M. Schrader",
            "Payload Lead": "Peter Dentch",
            "Logistics Officer": "Jacob Koslow",
            "Outreach Officer 1": "Christopher Renfro",
            "Outreach Officer 2": "Ian Scott",
        }
    }
    return render(request, "hprc/project.html", context)