# Project 1
#
# Name: Nathan Diekema
# Instructor: Padlipsky
# Section: 03

from math import *
from funcs import *


def main():

    massSkater = poundsToKG(float(input("How much do you weigh (pounds)? ")))
    distance = float(input("How far away is your professor (meters)? "))
    massObject = getMassObject(input("Will you throw a rotten (t)omato, banana cream (p)ie, (r)ock, (l)ight saber, or lawn (g)nome? "))

    velocityObject = float(getVelocityObject(distance))

    velocitySkater = float(getVelocitySkater(massSkater, massObject, velocityObject))

    velocity = velocitySkater
    mass = massObject

    print("\nNice throw! ", end="")
    if mass <= 0.1:
        print("You're going to get an F!")
    elif mass > 0.1 and mass <= 1.0:
        print("Make sure your professor is OK.")
    elif mass > 1.0:
        if distance < 20:
            print("How far away is the hospital?")
        elif distance >= 20:
            print("RIP professor.")
    print("Velocity of skater: " + "{0:.3f}".format(velocitySkater) + " m/s")
    if velocity < 0.2:
        print("My grandmother skates faster than you!")
    elif velocity >= 0.2 and velocity < 1.0:
        pass
    elif velocity >= 1.0:
        print("Look out for that railing!!!")                    


if __name__ == '__main__':
    main()
