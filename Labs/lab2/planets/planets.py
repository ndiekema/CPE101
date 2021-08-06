def weight_on_planets():
   weight = input('What do you weigh on earth? ')
   weight = float(weight)
   mars = weight * .38
   jupiter = weight * 2.34
   print("On Mars you would weigh", mars, "pounds" +
           "\nOn Jupiter you would weigh", jupiter, "pounds")
   
   
   
if __name__ == '__main__':
   weight_on_planets()
