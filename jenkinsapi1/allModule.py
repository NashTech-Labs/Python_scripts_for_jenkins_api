#!/usr/bin/env python3
import os
import jenkins
import requests
import time
name = input('Enter username \n')
password = input('Enter password \n')
server = jenkins.Jenkins('http://localhost:8080', username=name, password=password)
os.system('clear')
def action():
    print("\t-----------------")
    print("\t  Choice ")
    data= ['Login','Jobcount','Buildjob',"buildstatus","logs"]
    for i in data:
        print("\t",i)
    opt=input("Enter options \n").lower()
    if opt== 'login':
        login()
    elif opt == 'jobcount':
        jobcount()
    elif opt == 'buildjob':
        buildjob()
    elif opt == 'buildstatus':
        print(buildstatus())
    elif opt == 'logs':
        logs()    
                       



def login():
    
    user= server.get_whoami()
    print('Hello %s successfully login' %(user['fullName']))

def jobcount():
      print (server.jobs_count())

def buildjob():
    job=input('Enter job name')
    server.build_job(job,token=password)


def buildstatus():
    response = requests.get('http://localhost:8080/job/firstjob/lastBuild/api/json', auth=('knoldus', '11492232de0db16d34836139cdb5ee45d3')).json()
    if response["building"]:
        return True
    else:
        return False   
def logs():
    while buildstatus():
       
      response = requests.get('http://localhost:8080/job/firstjob/lastBuild/logText/progressiveText?start=0', auth=('knoldus', '11492232de0db16d34836139cdb5ee45d3'))
      print(response.text)
      time.sleep(1)
      os.system('clear')
    print(response.text)  
# # jobcount()
action()