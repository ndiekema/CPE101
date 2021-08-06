# Project 5: Earthquakes
# Author: Nathan Diekema
# Instructor: Padlipsky

from urllib.request import *
from json import *
from datetime import *
from operator import *

# GIVEN FUNCTIONS:
# Use these two as-is and do not change them
def get_json(url):
   ''' Function to get a json dictionary from a website.
       url - a string'''
   with urlopen(url) as response:
      html = response.read()
   htmlstr = html.decode("utf-8")
   return loads(htmlstr)

def time_to_str(time):
   ''' Converts integer seconds since epoch to a string.
       time - an int '''
   return datetime.fromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S')   

def epsilon_equal(n, m, epsilon=0.00001):
   return (n - epsilon) < m and (n + epsilon > m)
def float_equal(n, m):
   return ("%.5f" % n) == ("%.5f" % m)
def string_equal(n,m):
   return n in m and m in n

# Add Earthquake class definition here   
class Earthquake:
   def __init__(self,place,mag,longitude,latitude,time):
      self.place = place
      self.mag = mag
      self.longitude = longitude
      self.latitude = latitude
      self.time = time

   def __eq__(self,other):
      placeCheck = string_equal(self.place,other.place)
      magCheck = float_equal(self.mag,other.mag)
      longitudeCheck = float_equal(self.time,other.time)
      latitudeCheck = float_equal(self.latitude,other.latitude)
      timeCheck = epsilon_equal(self.time,other.time)

      return magCheck and placeCheck and longitudeCheck and latitudeCheck and timeCheck

# Required function - implement me!   
def read_quakes_from_file(filename):
   file = open(filename, 'r')
   qls = []
   quakes = []
   for line in file:
      qls = line.strip().split(' ')
      magnitude = float(qls[0])
      longitude = float(qls[1])
      latitude = float(qls[2])
      time = int(qls[3])
      place = ' '.join(qls[4:])
      newQuake = Earthquake(place, magnitude, longitude, latitude, time)
      quakes.append(newQuake)
   file.close()
   #print(quakes)
   return quakes

#read_quakes_from_file("quakes.txt")

def print_quakes(quakes):
   print("Earthquakes:\n" + "------------\n")
   for q in quakes:
      mag = str("(" + ("%.2f" % q.mag) + ")")
      longitude = "%8.3f" % q.longitude
      latitude = "%7.3f" % q.latitude
      time = time_to_str(q.time)
      place = q.place
      #print(mag, "%+40s" % place, "at", time, "(" + "%8f" % longitude + ", " + "%7f" % latitude + ")")
      print(mag, "%+40s" % place, "at", time, "(" + longitude + "," + latitude + ")")

def display_options():
   option = input("\nOptions:\n" + "  (s)ort\n" + "  (f)ilter\n" + "  (n)ew quakes\n" + "  (q)uit\n\n" + "Choice: ")
   while option not in "sSfFnNqQ":
      option = input("\nOptions:\n" + "  (s)ort\n" + "  (f)ilter\n" + "  (n)ew quakes\n" + "  (q)uit\n\n" + "Choice: ")
   return option

def sort_quakes(quakes):
   sortedList = []
   option = input("Sort by (m)agnitude, (t)ime, (l)ongitude, or l(a)titude? ")
   if option in "mM":
      sortedList = sorted(quakes, key = lambda quake: quake.mag, reverse = True)
   elif option in "tT":
      sortedList = sorted(quakes, key = lambda quake: quake.time, reverse = True)
   elif option in "lL":
      sortedList = sorted(quakes, key = lambda quake: quake.longitude, reverse = True)
   elif option in "aA":
      sortedList = sorted(quakes, key = lambda quake: quake.latitude, reverse = False)
   else:
      pass
   return sortedList

def quit(quakes):
   file = open("quakes.txt", 'w')
   for q in quakes:
      file.write(str(q.mag) + " ")
      file.write(str(q.longitude) + " ")
      file.write(str(q.latitude) + " ")
      file.write(str(q.time) + " ")
      file.write(str(q.place) + "\n")
   file.close()

# Required function - implement me!
def filter_by_mag(quakes, low, high):
   filtered = []
   for q in quakes:
      mag = q.mag
      if mag >= float(low) and mag <= float(high):
         filtered.append(q)
   return filtered
      
# Required function - implement me!
def filter_by_place(quakes, word): 
   filtered = []
   for q in quakes:
      place = q.place
      if word.lower() in place.lower():
         filtered.append(q)
   return filtered

# Required function for final part - implement me too!   
def quake_from_feature(feature):
   newQuake = []
   mag = feature["properties"]["mag"]
   place = feature["properties"]["place"]
   time = (feature["properties"]["time"] // 1000)
   longitude = feature["geometry"]["coordinates"][0]
   latitude = feature["geometry"]["coordinates"][1]
   newQuake = Earthquake(place, mag, longitude, latitude, time)
   return newQuake

def output_updated(quakes):
   print("\nEarthquakes:\n" + "------------\n")
   for q in quakes:
      mag = str("(" + ("%.2f" % q.mag) + ")")
      longitude = "%.3f" % q.longitude
      latitude = "%.3f" % q.latitude
      time = time_to_str(q.time)
      place = q.place

      print(mag, "%+40s" % place, "at", time, "(" + "%8f" % longitude + ", " + "%7f" % latitude + ")")



      #REORGANIZING LIST [PROJECT 4]
   # newList = []
   # found = True
   # for current in range(len(words)): #for each given word
   #     for lists in foundWords:    #for each list in found words
   #         if lists[0] == words[current]:
   #             newList.append(lists)
   #     if len(newList) == 0:
   #             newList.append([words[current]])
   #     else:
   #         if newList[-1][0] != words[current]:
   #             newList.append([words[current]])