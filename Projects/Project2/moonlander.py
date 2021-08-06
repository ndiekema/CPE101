# Project 2 - Moonlander
# Author: Nathan Diekema
# Instructor: Padlipsky

from landerFuncs import *

showWelcome()
altitude = getAltitude()
currentFuel = getFuel()
velocity = 0.00
elapsedTime = 0
fuelRate = 0
acceleration = 0

while currentFuel > 0 and altitude > 0:
	displayLMState(elapsedTime, altitude, velocity, currentFuel, fuelRate)
	fuelRate = getFuelRate(currentFuel)
	currentFuel = updateFuel(currentFuel, fuelRate)
	acceleration = updateAcceleration(1.62, fuelRate)
	altitude = updateAltitude(altitude, velocity, acceleration)
	velocity = updateVelocity(velocity, acceleration)
	elapsedTime += 1

while currentFuel <= 0 and altitude > 0:
	print("OUT OF FUEL - " + ("%+10s %3d %s %7.2f %s %7.2f" % ("Elapsed Time:", elapsedTime, "Altitude:",  altitude, "Velocity:", velocity)))
	#print("OUT OF FUEL - " + "Elapsed Time:" + str("%7.2f" % elapsedTime) + " Altitude: " +  str("%7.5f" % altitude) + " Velocity: " + str("%7.4f" % velocity))
	acceleration = -1.62
	altitude = updateAltitude(altitude, velocity, acceleration)
	velocity = updateVelocity(velocity, acceleration)
	elapsedTime += 1
	fuelRate = 0

print("\nLM state at landing/impact")
displayLMState(elapsedTime, altitude, velocity, currentFuel, fuelRate)
displayLMLandingStatus(velocity)