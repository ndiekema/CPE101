import unittest
from landerFuncs import *

class TestCases(unittest.TestCase):
#Update Acceleration
   def test_update_acc1(self):
      self.assertAlmostEqual(updateAcceleration(1.62, 0), -1.62)          
   def test_update_acc2(self):
      self.assertAlmostEqual(updateAcceleration(1.62, 9), 1.296)
#Update Altitude
   def test_update_alt1(self):
   	  self.assertAlmostEqual(updateAltitude(1000, -8, 1.62), 992.81)
   def test_update_alt2(self):
   	  self.assertAlmostEqual(updateAltitude(2500, 15, -8), 2511)
#Update Velocity
   def test_update_vel1(self):
   	  self.assertAlmostEqual(updateVelocity(0,0),0)
   def test_update_vel2(self):
   	  self.assertAlmostEqual(updateVelocity(9,1.62), 10.62)
#Update Fuel

   def test_update_fuel1(self):
   	  self.assertAlmostEqual(updateFuel(0,0), 0)
   def test_update_fuel2(self):
   	  self.assertAlmostEqual(updateFuel(1000,9),991)

      

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

