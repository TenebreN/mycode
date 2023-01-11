#!/usr/bin/env python3
''' farm animals | VArmstrong '''


farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]


Farmcontents= farms[0]["agriculture"]

for x in Farmcontents:
    print(x)

for farm in farms:
    print("-" , farm["name"])
farmchoice = input("pick a farm! \n")

for farm in farms:
    if farm["name"].lower() == farmchoice.lower():
        print(f"{farmchoice} specializes in {agriculture}")
