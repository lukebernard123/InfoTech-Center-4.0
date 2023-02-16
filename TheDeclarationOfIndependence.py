# Programmer: Mr.Lange
# Date: 2.16.2023
# Program: Infotech Center Upgrades

"""
We will make a temperature function that changes with the temperature 
outside
"""

#Import Libraries Here
import random 



def temperature():
    weatherForcast = ["10-30","9-","31-50","51-59","60-70","70+"]
    weatherCondition = random.choice(weatherForcast)
    return weatherCondition 


def carTemp():
    if temperature() == "10-30":
        print("\n Car Temp has been increased by 15 degrees Farenheit due to colder temp!.",)
    elif temperature() == "9-":
        print("\n Car Temp has been increased by 20 degrees due to Blizzard Temps",)
    elif temperature() == "31-50":
        print("\n Car Temp has been increased by 5 degrees due to rainy conditions",)
    elif temperature() == "51-59":
        print("\n Car Temp has been increased by 0 degrees due to Foggy conditions",)
    elif temperature() == "60-70":
        print("\n Car Temp has been increased by 5 degrees due to Windy conditions",)
    elif temperature() == "70+":
        print("\n Car Temp has been decerased by 10 degrees due to Nomral conditions. Have a good day!",)

carTemp()
    