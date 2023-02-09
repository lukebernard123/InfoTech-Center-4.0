# Date: 2.8.2023
# Program: Weather System Updates
# Programmer: Mr.Lange
#Create weather condition in a list and choose it randomly 
#Import Libraries Here
import random 

def weather():
    weatherForcast = ["Snowing","Blizzard","Raining","Foggy","Windy","Icy","Sunshine"]
    weatherCondition = random.choice(weatherForcast)
    return weatherCondition 

# Variable to call weather() once in our VRS
weatherAlert = weather()

print(weatherAlert)



# VRS () to respond to the weather conditions 
def VehicleResponseSystem():
    print("HOWDY")

   