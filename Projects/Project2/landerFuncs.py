# Project 2 - Moonlander
# Author: Nathan Diekema
# Instructor: Padlipsky

def showWelcome():
    welcome = ("\nWelcome aboard the Lunar Module Flight Simulator\n\n" +
     "   To begin you must specify the LM's initial altitude\n" +
     "   and fuel level.  To simulate the actual LM use\n" +
     "   values of 1300 meters and 500 liters, respectively.\n\n" +
     "   Good luck and may the force be with you!\n")
    print(welcome)
   
def getFuel():
    value = int(input("Enter the initial amount of fuel on board the LM (in liters): "))
    while value <= 0:
        print("ERROR: Amount of fuel must be positive, please try again")
        value = int(input("Enter the initial amount of fuel on board the LM (in liters): "))
        
    return value

def getAltitude():
    altitude = float(input("Enter the initial altitude of the LM (in meters): "))
    while altitude <= 0 or altitude > 9999:
        print("ERROR: Altitude must be between 1 and 9999, inclusive, please try again")
        altitude = float(input("Enter the initial altitude of the LM (in meters): "))

    return altitude
        
   
def displayLMState(elapsedTime, altitude, velocity, fuelAmount, fuelRate):
   if elapsedTime == 0:
    	print("\nLM state at retrorocket cutoff")
   print("%+13s %4d" % ("Elapsed Time:", elapsedTime) + " s")
   print("%+13s %4d" % ("Fuel:", fuelAmount) + " l")
   print("%+13s %4d" % ("Rate:", fuelRate) + " l/s")
   print("%+13s %7.2f" % ("Altitude:", altitude) + " m")
   print("%+13s %7.2f" % ("Velocity:", velocity) + " m/s")
   print('')


def getFuelRate(currentFuel):
    fuelRate = int(input("Enter fuel rate (0-9, 0=freefall, 5=constant velocity, 9=max thrust): "))
    while fuelRate > currentFuel or fuelRate > 9 or fuelRate < 0:
        if fuelRate > 9 or fuelRate < 0:
            print("ERROR: Fuel rate must be between 0 and 9, inclusive")
            fuelRate = int(input("Enter fuel rate (0-9, 0=freefall, 5=constant velocity, 9=max thrust): "))
        elif fuelRate > currentFuel:
        	fuelRate = currentFuel
        else:
            fuelRate = 0
    return fuelRate

 
def updateAcceleration(gravity, fuelRate):
   acceleration = float(gravity * ((fuelRate / 5) - 1))
   return acceleration
	
def updateAltitude(altitude, velocity, acceleration):
   altitude1 = altitude + velocity + (acceleration / 2)
   if altitude1 < 0:
      altitude1 = 0
   return altitude1
   
def updateVelocity(velocity, acceleration):
   velocity1 = velocity + acceleration
   return velocity1

def updateFuel(fuel, fuelRate):
   fuel1 = fuel - fuelRate
   return fuel1

def displayLMLandingStatus(velocity):
	if velocity <= 0 and velocity >= -1:
		print("\nStatus at landing - The eagle has landed!")
	elif velocity < -1 and velocity >= -10:
		print("\nStatus at landing - Enjoy your oxygen while it lasts!")
	else:
		print("\nStatus at landing - Ouch - that hurt!")
