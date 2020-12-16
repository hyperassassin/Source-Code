import datetime
import time
import requests
from plyer import notification

covidData = None
try:
    covidData = requests.get("https://corona-rest-api.herokuapp.com/Api/india")
except:
    print("Please !! Check Your Internet Connection")

if(covidData != None):
    data = covidData.json()['Success']
    while(True):
        notification.notify(
            title = "COVID19 Stats on {}".format(datetime.date.today()),
            message = "Total cases : {totalcases}\n Today cases : {todaycases}\n Today deaths : {todaydeaths}\n Total active : {active}\n Recovered : {recovered}\n Total Tests : {totaltests}".format(
                                    totalcases = data['cases'],
                                    todaycases = data['todayCases'],
                                    todaydeaths = data['todayDeaths'],
                                    active = data['active'],
                                    recovered = data['recovered'],
                                    totaltests = data['totalTests']),
            app_icon = "D:\Python\icon.ico",
            timeout = 50)
        time.sleep(60*60*4)
