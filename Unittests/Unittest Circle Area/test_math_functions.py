import unittest
import math_functions
from math import pi

class KnownValues(unittest.TestCase):
    def test_areaCircle_for_10_radius(self):
        #the result area of a circle with radius10
        result = math_functions.areaCircle(10)
        #expected to be 314...
        expected = 314.1592653589793
        #test if the expected is equal to result
        self.assertEqual(expected,result)
    
    def test_areaCircle_for_2_radius(self):
        #the result area of a circle with radius2
        result = math_functions.areaCircle(2)
        #expected to be 314...
        expected = 12.566370614359172
        #test if the expected is equal to result
        self.assertEqual(expected,result)

    def test_areaCircle_for_500_radius(self):
        #the result area of a circle with radius2
        result = math_functions.areaCircle(500)
        #expected to be 314...
        expected = 785398.1633974483
        #test if the expected is equal to result
        self.assertEqual(expected,result)
    
    def test_areaCircle_other_cases(self):
        self.assertAlmostEqual(math_functions.areaCircle(1),pi)
        self.assertAlmostEqual(math_functions.areaCircle(0),0)
        self.assertAlmostEqual(math_functions.areaCircle(2.1),pi*2.1**2)
    
    def test_values(self):
        self.assertRaises(ValueError,math_functions.areaCircle,-2)
    
    def test_types(self):
        self.assertRaises(TypeError,math_functions.areaCircle,3+5j)
        self.assertRaises(TypeError,math_functions.areaCircle,True)
        self.assertRaises(TypeError,math_functions.areaCircle,"radius")

if __name__ == '__main__':
    unittest.main()

