from django.shortcuts import render


def index(request):
    context = {'nbar': 'home'}
    return render(request, "hprc/index.html", context)

def sponsors(request):
    context = {'nbar': 'sponsors'}
    return render(request, "hprc/sponsors.html", context)

def construction(request):
    context = {'nbar': 'dog'}
    return render(request, "hprc/construction.html", context)

def contact(request):
    context = {'nbar': 'contact'}
    return render(request, "hprc/contact.html", context)

def donate(request):
    context = {'nbar': 'donate'}
    return render(request, "hprc/donate.html", context)
    
def team(request):
    context = {'nbar': 'team'}
    return render(request, "hprc/team.html", context)

def media(request):
    context = {'nbar': 'media'}
    return render(request, "hprc/media.html", context)

def present(request):
    context = {'nbar': 'present'}
    return render(request, "hprc/present.html", context)

def sponsorpackage(request):
    context = {'nbar': 'sponsors',
                'docName': 'Sponsorship Package',
                'document': 'hprc/pdfs/sponsorship_package.pdf',
                'docUrl': 'hprc:sponsorpackage'}
    return render(request, "hprc/pdfviewer.html", context)

def presentposters(request):
    context = {'nbar': 'media',
                'docName': 'Presentation Night Posters',
                'document': 'hprc/pdfs/presentation_posters.pdf',
                'docUrl': 'hprc:presentposters'}
    return render(request, "hprc/pdfviewer.html", context)

def apr22(request):
    context = {'nbar': 'media',
                'docName': 'April 2022 Newsletter',
                'document': 'hprc/pdfs/Apr22.pdf',
                'docUrl': 'hprc:apr22'}
    return render(request, "hprc/pdfviewer.html", context)

def mar22(request):
    context = {'nbar': 'media',
                'docName': 'March 2022 Newsletter',
                'document': 'hprc/pdfs/Mar22.pdf',
                'docUrl': 'hprc:mar22'}
    return render(request, "hprc/pdfviewer.html", context)

def feb22(request):
    context = {'nbar': 'media',
                'docName': 'February 2022 Newsletter',
                'document': 'hprc/pdfs/Feb22.pdf',
                'docUrl': 'hprc:feb22'}
    return render(request, "hprc/pdfviewer.html", context)

def decjan22(request):
    context = {'nbar': 'media',
                'docName': 'December & January 2022 Newsletter',
                'document': 'hprc/pdfs/DecJan22.pdf',
                'docUrl': 'hprc:decjan22'}
    return render(request, "hprc/pdfviewer.html", context)

def nov21(request):
    context = {'nbar': 'media',
                'docName': 'November 2021 Newsletter',
                'document': 'hprc/pdfs/Nov21.pdf',
                'docUrl': 'hprc:nov21'}
    return render(request, "hprc/pdfviewer.html", context)

def oct21(request):
    context = {'nbar': 'media',
                'docName': 'October 2021 Newsletter',
                'document': 'hprc/pdfs/Oct21.pdf',
                'docUrl': 'hprc:oct21'}
    return render(request, "hprc/pdfviewer.html", context)

def sept21(request):
    context = {'nbar': 'media',
                'docName': 'September 2021 Newsletter',
                'document': 'hprc/pdfs/Sept21.pdf',
                'docUrl': 'hprc:sept21'}
    return render(request, "hprc/pdfviewer.html", context)

def april21(request):
    context = {'nbar': 'media',
                'docName': 'April 2021 Newsletter',
                'document': 'hprc/pdfs/April21.pdf',
                'docUrl': 'hprc:april21'}
    return render(request, "hprc/pdfviewer.html", context)

def may21(request):
    context = {'nbar': 'media',
                'docName': 'May 2021 Newsletter',
                'document': 'hprc/pdfs/May21.pdf',
                'docUrl': 'hprc:may21'}
    return render(request, "hprc/pdfviewer.html", context)

def capricornus(request):
    context = {
        'nbar': "projects",
        "project_title": "Capricornus",
        "year": "2022-2023",
        "docs": {
            "Sponsorship Presentation": "hprc/capricornus/2023_Sponsor_Project_Presentation.pdf",
        },
        # "photos": "",
        "sponsors": {
            "Platinum": [
                "Altium",
		        "Test Devices Inc.",
		        "WPI Giving Day Donors"
             ],
             "Gold": [
                "WPI Tinkerbox",
                "Ensign-Bickford Aerospace & Defense",
		        "Collins Aerospace",
                "enDAQ"
             ],
             "Silver": [
                "Blue Origin",
                "Atomic Machines"
             ]
         },
        "image": 'hprc/capricornus/machining-test.jpg',
        "caption": "Members of the structures subteam practice their machining skills.",
        "text": [
            (
                "In the team's fifth year, WPI HPRC will compete for the second time in the Intercollegiate Rocket "
                "Engineering Competition (IREC) in the 10,000 ft COTS category. "
                "The project is named Capricornus, the goat constellation. "
                "The rocket is named after the brightest star in the constellation, Deneb, and the payload is named Nashira."
            ),
            (
                "The rocket will be 145 inches long with a diameter of 6 inches and features improvements to the recovery system, "
                "fin can, and airbrakes system. Based on our experience from the previous year, numerous improvements are being "
                "implemented for our novel coupling system. The airbrakes will again be used to target an apogee of 10,000 feet."
            ),
            (
                "This year's payload is a quadcopter, whose retention system detaches from the rocket during descent and continues descending under its own parachute. "
                "Once the retention system reaches a certain altitude, it will release the quadcopter to perform its primary mission. "
                "The quadcopter releases a series of three cubes that feature integrated weather sensors and telemetry "
                "and will transmit information back to the ground station. The mission will be fully autonomous with monitoring via an FPV system."
            ),
        ],
        "officers": {
            "Captain": "Kevin Schultz",
            "Rocket Lead": "Terence Tan",
            "Payload Lead": "Jake Roller",
            "Electronics Lead": "Michael Beskid",
            "Safety Officer": "Haggay Vardi",
            "Treasurer": "Aunika Yasui",
            "Logistics Officer": "Sarah Semy",
            "Sponsorship Officer": "Peter Korfuzi",
            "Documentation Officer": "Jon Whooley",
            "Engagement Officer": "Navpreet Kaur",
            "Public Relations Officer": "Natanel Pinkhasov", 
        }
    }
    return render(request, "hprc/project.html", context)
    
def aquila(request):
    context = {
        'nbar': "projects",
        "project_title": "Aquila",
        "year": "2021-2022",
        "docs": {
            "Technical Report": "hprc/aquila/81_technical_report.pdf",
            "Podium Presentation": "hprc/aquila/81_podium_presentation.pdf",
            "Failure Report": "hprc/aquila/81_failure_investigation_report.pdf",
        },
        "photos": "https://photos.app.goo.gl/pJg9oeSU6WWET1Qs7",
        "sponsors": {
            "Platinum": [
                "Altium"
            ],
            "Gold": [
                "WPI Tinkerbox",
                "Ensign-Bickford Aerospace & Defense",
                "enDAQ"
            ],
            "Bronze": [
                "Astralintu",
                "Test Devices Inc.",
                "Collins Aerospace",
                "Turner Construction"
            ]
        },
        "image": 'hprc/aquila/design-review-dec21.jpg',
        "caption": "Members of the airbrakes subteam present their design during the internal design review.",
        "text": [
            (
                "Now in the team’s fourth year, WPI HPRC looked to reach new heights, literally and figuratively "
                "by competing in the Intercollegiate Rocket Engineering Competition (IREC) in "
                "the 10,000 ft COTS category. The team grew to around 110 members, and was prepared to take on "
                "the challenge of creating a more powerful rocket. The project was named Aquila, after a constellation "
                "that contains the starts Altair and Tarazed. Altair means eagle in Latin."
            ),
            (
                "The rocket, Altair, measured 134 inches long with a diameter of 6 inches and featured "
                "redesigned couplings and airbrakes. The new couplings hold together parts of the airframe that "
                "do not separate in flight by using a screw-together mechanisim meant to provide proper stiffness "
                "and support. The airbrake system was used to target an apogee of 10,000 feet."
            ),
            (
                "The payload, Tarazed, was a quadcopter designed to locate the rocket after the rocket lands by "
                "triangulating a signal broadcast by the rocket. It was designed verify the correct location using "
                "GPS data and subsequently relay its position back to the ground crew."
            ),
            (
                "The team successfully made it to launch week in first year at IREC, a feat not accomplished by every "
                "team. After passing safety inspection Altair and Tarazed launched on the second day of launches, "
                "however the vehicle broke apart at burnout due to an incorrectly programmed altimeter. Despite the "
                "failure, the team gained significant experience from launch week, and from the failure analysis process. "
                "Within the 10k COTS category, WPI HPRC placed 3rd in technical report quality, and 11th in design quality. "
                "Additionally, the team received the Sportsmanship Award. "
            )
        ],
        "officers": {
            "Captain": "Kevin Schultz",
            "Rocket Lead": "Troy Otter",
            "Payload Lead": "Jake Roller",
            "Safety Officer": "Paul Coccomo",
            "Treasurer": "Giovanni Giacalone",
            "Logistics Officer": "Bridget Wirtz",
            "Sponsorship Officer": "Julia Sheats",
            "Documentation Officer": "Christian M. Schrader",
            "Engagement Officer": "Kirsten Bowers",
            "Public Relations Officer": "Abby Hyde", 
        }
    }
    return render(request, "hprc/project.html", context)

def sirius(request):
    context = {
        'nbar': "projects",
        "project_title": "Sirius and Polaris",
        "year": "2020-2021",
        "docs": {
            "Proposal": "hprc/sirius/WPI HPRC Proposal 2021.pdf",
            "Preliminary Design Review": "hprc/sirius/WPI HPRC PDR 2021.pdf",
            "PDR Presentation": "hprc/sirius/WPI HPRC PDR Presentation 2021.pdf",
            "Critical Design Review": "hprc/sirius/WPI HPRC CDR 2021.pdf",
            "CDR Presentation": "hprc/sirius/WPI HPRC CDR Presentation 2021.pdf",
        },
        "photos": "https://photos.app.goo.gl/w3eEeHMk1ChAUU8x5",
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
                "Entering their third year, WPI USLI made the decision to rebrand to the High Power Rocketry Club (HPRC). "
                "This year was uniquely challenging as the COVID-19 pandemic prevented the majority of in-person meetings. "
                "While the team initially continued to compete in NASA Student Launch, the team dropped out of the competition in December "
                "as there was no way for the team to fulfill launch requirements while staying in compliance with WPI's and the CDC's "
                "COVID safety guidelines. Despite this, the team continued designing and building our rocket and payload through "
                "the end of the year. The team was finally able to launch the 2021 rocket at St. Albans in April 2022 to test several systems "
                "for the 2022 project, Aquila. "
            ),
            (
                "The team's rocket, Sirius, continued to build upon the experience gained in the past two competition years. "
                "It contained many new systems such as forward mounted motor retention, an airbrake system, and a custom "
                "avionics board. The vehicle has a predicted apogee of 4934 ft but has a target apogee of 4550 ft. "
                "To ensure there is no overshoot, the airbrake system is actively controlled by the avionics to produce "
                "just enough drag to reduce the vehicle's apogee to the target."
            ),
            (
                "The vehicle's payload is a lander designated Polaris. After being ejected from the vehicle during descent, Polaris "
                "lands under its own parachute before engaging its self-righting system which rights the payload from any "
                "orientation using a set of outward folding petals. This is more finely adjusted by the stabilization system "
                "which uses a set of legs that deploy to level the payload within 5 degrees on uneven terrain. Finally, "
                "it takes a panoramic photo using a top mounted camera before transmitting the photo back to the ground station."
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
                "The goal of the payload, named Icarus, was to mechanically retain and deploy an Unmanned Aerial Vehicle "
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
                "Officer Board, the team received its initial funding.  The project name, G.O.A.T.S was selected in honor of WPI's "
                "mascot, Gompei the Goat.  Having just started out, the members "
                "of the team lacked experience.  The officers were mostly sophomores leading a large "
                "group of mostly freshmen.  Despite this, the team spent the year learning and overcoming "
                "challenges at every step.  They submitted their first design reviews, solved unexpected "
                "vehicle packing problems at their subscale launch, and even rebuilt the entire lower airframe "
                "in a week after its loss due to bulkhead failure on its first test flight."
            ),
            (
                "While not every rookie team makes it to launch week, WPI got there, beating many tough challenges "
                "along the way.  Ultimately, when the team's rocket took flight at the competition launch in Huntsville, "
                "it was destroyed at around 800 ft due to a defect in the motor the team purchased.  While it may have "
                "been disappointing, the team still returned home excited.  The members learned a lot from meeting with "
                "other teams and NASA engineers and were already brainstorming new ideas for next year before launch week "
                "was over.  The first year was not perfect, but it cemented the team as WPI's premier rocketry team."
            ),
            (
                "Our first launch vehicle, named Batman, was designed to reach an apogee of approximately " 
                "4094 ft and split into four independent sections "
                "over the course of its descent. The four sections of the rocket were the upper airframe, the lower "
                "airframe, the payload retention system, and the nose cone, which descended separately from the other three sections. "
                "The upper airframe housed the payload retention system for the duration of its flight and released it "
                "during descent so the payload mission could be performed. The vehicle had three "
                "parachutes, a nose cone parachute, drogue parachute and main parachute. The launch vehicle’s "
                "flight data was recorded using a Raven 3 Altimeter that was housed in the electronics bay."
            ),
            (
                "Our payload, named Robin, was a quadrotor UAV housed within a cylindrical "
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