import unittest
from customer import Customer
from rental import Rental
from pricecode import PriceCode


class RentalTest(unittest.TestCase):
	
	def setUp(self):
		self.new_movie = PriceCode("Mulan", PriceCode.new_release)
		self.regular_movie = PriceCode("CitizenFour", PriceCode.normal)
		self.childrens_movie = PriceCode("Frozen", PriceCode.childrens)

	def test_movie_attributes(self):
		"""trivial test to catch refactoring errors or change in API of Movie"""
		m = PriceCode("CitizenFour", PriceCode.normal)
		self.assertEqual("CitizenFour", m.get_title())
		self.assertEqual(PriceCode.normal, m.get_price_code())

	@unittest.skip("TODO add this test when you refactor rental price")
	def test_rental_price(self):
		rental = Rental(self.new_movie, 1)
		self.assertEqual(rental.get_price(), 3.0)
		rental = Rental(self.new_movie, 5)
		self.assertEqual(rental.get_price(), 15.0)
		self.fail("TODO add more tests for other movie categories")

	@unittest.skip("TODO add test of frequent renter points when you add it to Rental")
	def test_rental_points(self):
		self.fail("TODO add  test of frequent renter points")