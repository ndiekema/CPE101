# Project 1
#
# Name: Nathan Diekema
# Instructor: Padlipsky
# Section: 03

from math import *


def poundsToKG(pounds):

    kilograms = pounds * 0.453592

    return kilograms


def getMassObject(object): 

    if object == 't':
       mass = 0.1
    elif object == 'p':
        mass = 1.0
    elif object == 'r':
        mass = 3.0
    elif object == 'g':
        mass = 5.3
    elif object == 'l':
        mass = 9.07
    else:
        mass = 0.0

    return mass


def getVelocityObject(distance):
        
    velocityObject = sqrt(9.8 * distance / 2)

    return velocityObject


def getVelocitySkater(massSkater, massObject, velObject):


    velocitySkater = float((massObject * velObject) / massSkater)


    return velocitySkater




