# Name : Vaibhav Gupta
# Roll No : 2019341
# Group : 9

import unittest
from a1 import changeBase

# TEST cases should cover the different boundary cases.

class testpoint(unittest.TestCase):
	
	def test_change_base(self):
		self.assertEqual(changeBase(100, "INR", "RON", "2011-10-31"), 6.358062718178886)
		self.assertAlmostEqual(changeBase(1, "INR", "GBP", "2009-10-25"), 0.014, delta = 0.001)
		self.assertEqual(changeBase(100, "EUR", "EUR", "1999-01-05"), 100)
		self.assertEqual(changeBase(1, "EUR", "MYR", "2019-08-25"), 4.636)
		self.assertAlmostEqual(changeBase(1.1564,"AUD","IDR","2009-08-20"), 9675.08, delta=0.01)
		self.assertAlmostEqual(changeBase(19.4526, "USD", "EUR", "2001-09-11"), 21.6, delta=0.2)
		self.assertEqual(changeBase(123456,"CHF","JPY","2005-03-21"), 11066959.938128382)
		# these are just sample values. You have to add testcases (and edit these) for various dates.
		# (don't use the current date as the json would keep changing every 4 minutes)
		# you have to hard-code the 2nd parameter of assertEquals by calculating it manually
		# on a particular date and checking whether your changeBase function returns the same
		# value or not.




if __name__=='__main__':
	unittest.main()