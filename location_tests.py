import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc1 = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc1),"Location('SLO', 35.3, -120.7)")
        loc2 = Location("Paris", 48.9, 2.4)
        self.assertEqual(repr(loc2),"Location('Paris', 48.9, 2.4)")

    def test_eq(self):
        loc1 = Location("SLO", 35.3, -120.7)
        loc2 = Location("Paris", 48.9, 2.4)
        self.assertNotEqual(loc1,loc2)
        loc3 = loc1
        self.assertEqual(loc1, loc3)

    def test_init(self):
        loc1 = Location("SLO", 35.3, -120.7)
        self.assertEqual(loc1.name, 'SLO')
        self.assertEqual(loc1.lat, 35.3)
        self.assertEqual(loc1.lon, -120.7)

    
    # Add more tests!

if __name__ == "__main__":
        unittest.main()
