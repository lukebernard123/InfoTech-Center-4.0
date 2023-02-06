
# Programmer: Luke Bernard
# Date Merged: 2.6.2023
# Merged welcome screen and gasoline branches - stable



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
        print('\n\n033[1;32;40m Mission Accomplished - Retina Scanned - Access Granted\n')



# Programmer: Luke Bernard
# Date: 1.20.2023
# Program: Infotech Center Upgrades


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
        print("***WARNING YOU ARE ON EMPTY***")
        sleep(1)
        print("Calling Emergency Contact")
    elif gasLevelIndicator == "Low":
        print("***Warning***")
        sleep(1)
        print("Your gas tank is extremely low, checking Google Maps for the closest gas station.")
        sleep(1)
        print("The closest gas station is,",listOfGasStations(),"which is", milesToGasStationLow,"miles away.")
    elif gasLevelIndicator == "QuarterTank":
        print("*** Warning***")
        sleep(1)
        print("Your gas tank is at a Quarter Tank and the closest gas station is", listOfGasStations(),"which is", milesToGasStationQuarterTank, "miles away.")
    elif gasLevelIndicator == "Half Tank":
        print("Your gas tank is a half of a tank full which is plenty of gas to make it to your destination today!")
    elif gasLevelIndicator == "Three Quarter Tank":
        print("Your gas tank is three quarters full, which is enough to reach your destination today.")
    else:
        print("Your gas tank is full - Yeah! Congrats - Vroom Vroom")







gasLevelAlert()







