import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CheckYoSelf.settings')
import django

django.setup()
from Chemicals.models import Topic, Group, Student

data = [
    {
        "title": "Birth Control",
        "description": "Is birth control solely used for the reason the media portrays the reason to be?",
        "groups": [
            {
                "members": [
                    "Camryn S",
                    "Marissa E",
                ],
                "poster": "../assets/chemicals/posters/Birth Control_MC.jpg"
            },
            {
                "members": [
                    "Annalisa T",
                    "Dayja M",
                ],
                "poster": "../assets/chemicals/posters/Birth Control_AD.jpg"
            },
        ],
    },
    {
        "title": "Bleach",
        "description": "Should bleach be used commonly in households?",
        "groups": [
            {
                "members": [
                    "Carter K",
                    "Ezekiel D",
                ],
                "poster": "../assets/chemicals/posters/Bleach_EC.jpg"
            },
        ],
    },
    {
        "title": "Caffeine",
        "description": "Is caffeine a net positive?\nShould there be restrictions on coffee?",
        "groups": [
            {
                "members": [
                    "Collin C",
                    "Ella T",
                ],
                "poster": "../assets/chemicals/posters/Caffeine_CE.jpg"
            },
            {
                "members": [
                    "Stella M",
                    "Sofia T",
                ],
                "poster": "../assets/chemicals/posters/Caffeine_SS.jpg"
            },
        ],
    },

    {
        "title": "DDT",
        "description": "Should DDT be used to combat Malaria, despite the enviornmental and health impacts?",
        "groups": [
            {
                "members": [
                    "Scott S",
                    "Jonas G",
                ],
                "poster": "../assets/chemicals/posters/DDT_SJ.jpg"
            },
        ],
    },
    {
        "title": "GMOs",
        "description": "Are GMO's bad for plants and animals?",
        "groups": [
            {
                "members": [
                    "Markus H",
                    "Max G",
                ],
                "poster": "../assets/chemicals/posters/GMOs_MM.jpg"
            },
            {
                "members": [
                    "Edward H",
                    "Allan B",
                ],
                "poster": "../assets/chemicals/posters/GMOs_EA.jpg"
            },
        ],
    },
    {
        "title": "Hydroxychloroquine",
        "description": "Is Hydroxychloroquine a possible cure for Covid-19?",
        "groups": [
            {
                "members": [
                    "Drew N",
                    "Lev F",
                ],
                "poster": "../assets/chemicals/posters/Hydroxychloroquine_DL.jpg"
            },
            {
                "members": [
                    "Zoe N",
                    "Lydia D",
                ],
                "poster": "../assets/chemicals/posters/Hydroxychloroquine_LZ.jpg"
            },
        ],
    },
    {
        "title": "Marijuana",
        "description": "Should Marijuana be fully legalized in the U.S.?\nIs Cannabis more helpful than harmful?",
        "groups": [
            {
                "members": [
                    "Adam S",
                    "Isabella V",
                ],
                "poster": "../assets/chemicals/posters/Marijuana_AI.jpg"
            },
            {
                "members": [
                    "Zahid M",
                    "Elizabeth G"
                ],
                "poster": "../assets/chemicals/posters/Cannabis_ZE.jpg"
            },
        ],
    },
    {
        "title": "Mercury",
        "description": "Is mercury safe to use for dental fillings?",
        "groups": [
            {
                "members": [
                    "Donovan T",
                    "Isaiah D"
                ],
                "poster": "../assets/chemicals/posters/Mercury_DI.jpg"
            },
        ],
    },
    {
        "title": "Milk",
        "description": "Is milk healthy?\nIs milk more harmful or beneficial to our health?",
        "groups": [
            {
                "members": [
                    "Tamsen B",
                    "Gene L",
                    "Jesse R",
                ],
                "poster": "../assets/chemicals/posters/Is Milk Healthy_ Controversial chemical poster T+J+G.jpg"
            },
            {
                "members": [
                    "Remi M",
                    "Jacob A",
                ],
                "poster": "../assets/chemicals/posters/Milk_RJ.jpg"
            },
        ],
    },
    {
        "title": "Morphine",
        "description": "Is morphine addicting?",
        "groups": [
            {
                "members": [
                    "Sasha W",
                    "Lori R",
                ],
                "poster": "../assets/chemicals/posters/Morphine_LS.jpg"
            },
        ],
    },
    {
        "title": "MSG",
        "description": "Is MSG harmful to our bodies?",
        "groups": [
            {
                "members": [
                    "Zane C",
                    "Taher H",
                    "Antonio M",
                ],
                "poster": "../assets/chemicals/posters/MSG_ZTA.jpg"
            },
        ],
    },
    {
        "title": "Nicotine",
        "description": "What's sad the truth about nicotine?",
        "groups": [
            {
                "members": [
                    "Diego H",
                    "Adonijah D"
                ],
                "poster": "../assets/chemicals/posters/Nicotine_AD.jpg"
            },
        ],
    },
    {
        "title": "Perfume",
        "description": "Does perfume cause skin damage?",
        "groups": [
            {
                "members": [
                    "Nithin R",
                    "Noah M"
                ],
                "poster": "../assets/chemicals/posters/Perfume_NN.jpg"
            },
        ],
    },
    {
        "title": "Sugar",
        "description": "How bad is sugar?",
        "groups": [
            {
                "members": [
                    "Bryce D",
                    "Dominika B",
                    "Mitchell L",
                ],
                "poster": "../assets/chemicals/posters/Sugar_DMB.jpg"
            },
        ],
    },
    {
        "title": "Sulfates",
        "description": "Are sulfates in cosmetics as harmful as people say they are?",
        "groups": [
            {
                "members": [
                    "Jillian H",
                    "Sophia P"
                ],
                "poster": "../assets/chemicals/posters/Sulfates_JS.jpg"
            },
        ],
    },
    {
        "title": "Tear Gas",
        "description": "What are the effects of tear gas?",
        "groups": [
            {
                "members": [
                    "Maleah T",
                    "Anna L",
                    "Tyrone K",
                ],
                "poster": "../assets/chemicals/posters/tear gas_MAT.jpg"
            },
        ],
    },
    {
        "title": "Turmeric",
        "description": "Is turmeric truly a miracle drug?",
        "groups": [
            {
                "members": [
                    "Easha A",
                    "Armin B",
                ],
                "poster": "../assets/chemicals/posters/Tumeric_AE.jpg"
            },
        ],
    },
    {
        "title": "Vaccines",
        "description": "Do vaccines actually cause autism?",
        "groups": [
            {
                "members": [
                    "Claire L",
                    "Liz BO",
                ],
                "poster": "../assets/chemicals/posters/Vaccines_CE.jpg"
            },
        ],
    },
    {
        "title": "Yellow 5",
        "description": "Is yellow 5 (tartazine) dangerous to our bodies?",
        "groups": [
            {
                "members": [
                    "Kras C",
                    "Zaria G",
                ],
                "poster": "../assets/chemicals/posters/Yellow 5_KZ.jpg"
            },
        ],
    },
]

for i in data:
    t = Topic(title=i['title'], description=i['description'])
    t.save()

    for x in i['groups']:
        p = 'https://exhibition-site-2020.mitchelllong2.repl.co' + x['poster'][2:]
        g = Group(topic=t, poster=p, likes=0, class_name='CHANGE ME')

        g.save()

        for q in x['members']:
            s = Student(group=g, first_name=q.split(' ')[0], last_initial=q.split(' ')[1][:1])
            s.save()
