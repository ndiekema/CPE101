# Project 5: Earthquakes
# Author: Nathan Diekema
# Instructor: Padlipsky

from quakeFuncs import *

#Read in quakes from file
quakes = read_quakes_from_file("quakes.txt")

#Initial print
print_quakes(quakes)

#userInput will be either s,f,n or q
userInput = display_options()

while userInput not in "qQ":
   if userInput in "sS":
      #option = input("Sort by (m)agnitude, (t)ime, (l)ongitude, or l(a)titude? ")
      quakes = sort_quakes(quakes)
      output_updated(quakes)
   elif userInput in "fF":
      option = input("Filter by (m)agnitude or (p)lace? ")
      if option in "mM":
         low = input("Lower bound: ")
         high = input("Upper bound: ")
         quakesTemp = filter_by_mag(quakes,low,high)
         output_updated(quakesTemp)
      elif option in "pP":
         word = input("Search for what string?: ")
         quakesTemp = filter_by_place(quakes,word)
         output_updated(quakesTemp)
      else:
         option = input("\nFilter by (m)agnitude or (p)lace? ")
   elif userInput in "nN":
      lenQuakes = len(quakes)
      print("tesT")
      dic = get_json('http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_hour.geojson')
      print("STupId")
      feature = dic["features"]
      for feat in feature:
         newQuake = quake_from_feature(feat)
         if newQuake not in quakes:
            quakes.append(newQuake)
      if len(quakes) > lenQuakes:
         print("\nNew quakes found!!!")
      output_updated(quakes)
   else: #unnecessary catch
      userInput = display_options()
   userInput = display_options()

quit(quakes)

