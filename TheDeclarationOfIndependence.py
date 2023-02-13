# Date: 2.8.2023
# Program: Weather System Updates
# Programmer: Mr.Lange
#Create weather condition in a list and choose it randomly 
#Import Libraries Here
import random 

def weather():
    weatherForcast = ["Snowing","Blizzard","Rain","Foggy","Windy","Icy","Sunshine"]
    weatherCondition = random.choice(weatherForcast)
    return weatherCondition 

# Variable to call weather() once in our VRS
weatherAlert = weather()






# VRS () to respond to the weather conditions 
def VehicleResponseSystem():
    if weatherAlert == "Snowing":
        print("\n NWS has changed your Alarm by 15 minutes because of the weather forcast of",weatherAlert)
        print("VRS has been engaged, only allowing your vehicle to go 45 MPH")
    elif weatherAlert == "Blizzard":
        print("\n NWS has changed your Alarm by 30 minutes because of the weather forcast of",weatherAlert)
        print("VRS has been engaged, only allowing your vehicle to go 35 MPH")
    elif weatherAlert == "Rain":
          print("\n NWS is calling for",weatherAlert),",please drive extra careful"
    elif weatherAlert == "Foggy":
          print("\n NWS is calling for",weatherAlert)," conditions, please drive extra careful"
    elif weatherAlert == "Windy":
          print("\n NWS is calling for",weatherAlert)," conditions, please drive extra careful"
    elif weatherAlert == "Icy":
          print("\n NWS has changed your Alarm by 60 minutes because of the weather forcast of",weatherAlert)
          print("VRS has been engaged only allowing your vehicle to go 25 MPH")
    else:
        print("\nNWS is calling for", weatherAlert,"drive safley and have a wonderful day!") 
          
VehicleResponseSystem()
        




   