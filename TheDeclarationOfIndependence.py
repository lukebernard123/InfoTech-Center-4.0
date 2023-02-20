# Programmer: Luke Bernard
# Date - 2/20/23





"""
Our Welcome Screen will start our program letting
drivers know that the InfoTechCenter 4.0 is loading

"""

#Import Libraries Here
import time
import sys      #I imported the system library for further use in code.
import random
from time import sleep

print('\n\033[1;34;48m Welcome to InfoTech Center 4.0')

x = 0
a = 0

time.sleep(2)
print('')


while x != 20:
    x += 1

    b = ("\033[1;33;40m InfoTech Center OS is Loading" + "." * a)
    a = a + 1
    sys.stdout.write('\r'+b) # \r prints a carriage return first, so `b` is printed on top of the previous line.
    time.sleep(0.5)
    if a == 4:
        a = 0
    if x == 20:
        print('\n\n Mission Accomplished - Retina Scanned - Access Granted\n')



# Programmer: Luke Bernard
# Date: 1.20.2023
# Program: Infotech Center Upgradesfuction


"""
We will create a Function that will tell us our Fuel Gauge Level
  - Create a List with Gas Levels
  - Randomize and choose from the list to determine our gas level

Create a Function to determine our closest gas stations
 - Create a List of gas stations
 - Randomly choose a gas station from the list

Create a Function to determine our gas level and closest gas station
  -Print Gas level
  -Print Closest gas station
"""



# Gas Level Function

def gasLevelGauge():
    gasLevelList = ["Empty","Low","Quarter Tank","Half Tank","Three Quarter Tank","Full Tank"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel

#Variable calling gasLevelGauge function to store its value
gasLevelIndicator = gasLevelGauge()


#List of Gas Stations Function

def listOfGasStations():
  gasStations = ["Shell","Costco","Buc-ee's","Speedway","7-11","Circle-K","Meijer","Marathon","KFC"]
  gasStationsNearby = random.choice(gasStations)
  return gasStationsNearby


# Determine Gas Level & Closest Gas Station

def gasLevelAlert():
    milesToGasStationLow = round(random.uniform(1,25),2)
    milesToGasStationQuarterTank = round(random.uniform(26, 50), 2)
    if gasLevelIndicator == "Empty":
        print("***WARNING YOU ARE ON EMPTY***\n")
        sleep(1)
        print("Calling Emergency Contact\n")
    elif gasLevelIndicator == "Low":
        print("***Warning***")
        sleep(1)
        print("Your gas tank is extremely low, checking Google Maps for the closest gas station.\n")
        sleep(1)
        print("The closest gas station is,",listOfGasStations(),"which is", milesToGasStationLow,"miles away.")
    elif gasLevelIndicator == "QuarterTank":
        print("*** Warning***")
        sleep(1)
        print("Your gas tank is at a Quarter Tank and the closest gas station is", listOfGasStations(),"which is", milesToGasStationQuarterTank, "miles away.")
    elif gasLevelIndicator == "Half Tank":
        print("Your gas tank is a half of a tank full which is plenty of gas to make it to your destination today!\n")
    elif gasLevelIndicator == "Three Quarter Tank":
        print("Your gas tank is three quarters full, which is enough to reach your destination today.\n")
    else:
        print("Your gas tank is full - Yeah! Congrats - Vroom Vroom\n")












# Date: 2.8.2023
# Program: Weather System Updates
# Programmer: Luke Bernard




def weather():
    weatherForcast = ["Snowing","Blizzard","Rain","Foggy","Windy","Icy","Sunshine"]
    weatherCondition = random.choice(weatherForcast)
    return weatherCondition 

# Variable to call weather() once in our VRS
weatherAlert = weather()






# VRS () to respond to the weather conditions 
def VehicleResponseSystem():
    if weatherAlert == "Snowing":
        print("\n NWS has changed your Alarm by 15 minutes because of the weather forcast of\n",weatherAlert)
        print("VRS has been engaged, only allowing your vehicle to go 45 MPH\n")
    elif weatherAlert == "Blizzard":
        print("\n NWS has changed your Alarm by 30 minutes because of the weather forcast of\n",weatherAlert)
        print("VRS has been engaged, only allowing your vehicle to go 35 MPH\n")
    elif weatherAlert == "Rain":
          print("\n NWS is calling for",weatherAlert),",please drive extra careful\n"
    elif weatherAlert == "Foggy":
          print("\n NWS is calling for",weatherAlert)," conditions, please drive extra careful\n"
    elif weatherAlert == "Windy":
          print("\n NWS is calling for",weatherAlert)," conditions, please drive extra careful\n"
    elif weatherAlert == "Icy":
          print("\n NWS has changed your Alarm by 60 minutes because of the weather forcast of\n",weatherAlert)
          print("VRS has been engaged only allowing your vehicle to go 25 MPH\n")
    else:
        print("\nNWS is calling for", weatherAlert,"drive safley and have a wonderful day!\n") 
          




#Call Functions Here
print("\nNational Weather Service is checking conditions....")
sleep(2)
VehicleResponseSystem()
print("\nChecking current gas levels...")
sleep(2)
gasLevelAlert()
        

# Programmer: Luke Bernard
# Date: 2.16.2023
# Program: Infotech Center Upgrades
"""
We will make a function that shows contacts
- Create a list of contacts
-Print all contacts
"""
# Libraries Here
import random
def contacts():
    contactList = ["Mom","Dad","Brother","Sister","Grandma","Grandpa","Aunt","Uncle",]
    currentContact = random.choice(contactList)
    return currentContact
print("Alert!", contacts(),"is calling.")


# Programmer: Luke Bernard
# Date: 1.20.2023
# Program: Infotech Center Upgrades

"""
We will make a function that chooses from multiple songs
and shows that it is playing
"""
# Libraries here
import random

def songs():
    songList = ["Bad Habit","Smells Like Teen Spirit","505","Beat It","24k Magic","Here Comes the Sun"]
    songPlaying = random.choice(songList)
    return songPlaying 
currentSong = songs()

def songOn():
    if currentSong == "Bad Habit":
        print("Bad Habit by Steve Lacy is currently playing.")
    elif currentSong == "Smells Like Teen Spirit":
        print("Smells Like Teen Spirit by Nirvana is currently playing.")
    elif currentSong == "505":
        print("505 by Arctic Monkeys is currently playing.")
    elif currentSong == "Beat It":
        print("Beat It by Michael Jackson is currently playing.")
    elif currentSong == "24k Magic":
        print("24k Magic by Bruno Mars is currently playing.")
    else:
        print("Here Comes the Sun by The Beatles is currently playing.")


songOn()


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
    

