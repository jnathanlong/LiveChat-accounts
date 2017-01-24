# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 15:58:01 2016

@author: jeremy.long
"""

#Import CSV Module
import csv

#import requests module
import requests
from requests.auth import HTTPBasicAuth


#LiveChat API Key Variable
LC_api = input("Please paste your API key here:  ")
url = "https://api.livechatinc.com/agents"
User_ID = input("Please enter your LiveChat username-email here:  ")
header = {"X-API-Version": "2"}

GET = requests.get(url, auth=(User_ID, LC_api), headers=header)

#Field name variables from the CSV
login = ''
name = ''
job_title = ''
login_status = ''
permission = ''
groups = ''

#CSV File object variables
csvfilename = 'WP Account Provisioning Worksheet.gsheet - LiveChat.csv'
csvfile = open(csvfilename, 'r')
fieldnames = ("login","name","job_title","login_status","permission","groups")
reader = csv.DictReader(csvfile, fieldnames)

Agent = {}

print("Adding new LiveChat Agents...")

for row in reader:
    Agent = {}
    Agent = row
    Agent['groups'] = [1, 4, 5]
    print(str(Agent))
    print("Adding " + str(Agent['name']) + "...")
    PUT = requests.post(url, auth=(User_ID, LC_api), headers=header, data=Agent)
    PUT.text

print("All Done!")
