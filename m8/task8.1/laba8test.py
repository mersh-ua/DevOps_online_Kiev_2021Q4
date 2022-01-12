import typing
import unittest
import laba8

class laba8test(unittest.TestCase):

  def test_discriminant(self):
    self.assertEqual(laba8.discriminant(0,0,0),None)    #1
    self.assertEqual(laba8.discriminant(5,0,5),-100)    #2
    self.assertEqual(laba8.discriminant(-2,-2,4),36)    #2
    self.assertEqual(laba8.discriminant(10,0,0),0)      #2

  def test_roots(self):
    self.assertEqual(laba8.roots(0,0,0),("'a' must have nonzero value - don't worry","be happy"))   #1
    self.assertEqual(laba8.roots(5,0,5),('Nonreal','Nonreal'))                                      #2
    self.assertEqual(laba8.roots(-2,-2,4),(1.0,-2.0))                                               #3
    self.assertEqual(laba8.roots(10,0,0),(-0.0,None))                                               #4

if __name__ == '__main__':
    unittest.main()