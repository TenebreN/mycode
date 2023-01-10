#!/usr/bin/env python3

import requests

#define the NEO URL:
NEOURL= "https://api.nasa.gov/neo//rest/v1/feed?"

#the follow function grabs the credentials from the previously created file

def returncreds():
    #grab creds
    with open("/home/student/nasa.creds", "r") as mycreds
    nasacreds = mycreds.read()

    startdate = input("please enter startdate in YYYY-MM-DD format")

