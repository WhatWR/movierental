import unittest
from customer import Customer
from rental import Rental
from movie import *


class RentalTest(unittest.TestCase):

    def setUp(self):
        self.c = Customer("Movie Mogul")
        self.catalog = MovieCatalog()
        self.new_movie = PriceCode("Mulan", PriceCode.new_release)
        self.regular_movie = PriceCode("CitizenFour", PriceCode.normal)
        self.childrens_movie = PriceCode("Frozen", PriceCode.childrens)

        self.price_code_new = PriceCode.for_movie(self.new_movie)

        self.price_code_regular = PriceCode.for_movie(self.regular_movie)
        self.price_code_children = PriceCode.for_movie(self.children_movie)


def test_movie_attributes(self):
    """trivial test to catch refactoring errors or change in API of Movie"""
    self.assertEqual("CitizenFour", self.new_movie.get_title())


def test_rental_price(self):
    """calculate movie rental price"""
    rental = Rental(self.new_movie, 1, self.price_code_new)
    self.assertEqual(rental.get_price(), 3.0)
    rental = Rental(self.new_movie, 5, self.price_code_new)
    self.assertEqual(rental.get_price(), 15.0)

    rental = Rental(self.regular_movie, 2, self.price_code_regular)
    self.assertEqual(rental.get_price(), 2)
    rental = Rental(self.regular_movie, 3, self.price_code_regular)
    self.assertEqual(rental.get_price(), 3.5)

    rental = Rental(self.children_movie, 3, self.price_code_children)
    self.assertEqual(rental.get_price(), 1.5)
    rental = Rental(self.children_movie, 5, self.price_code_children)
    self.assertEqual(rental.get_price(), 4.5)


def test_rental_points(self):
    rental = Rental(self.new_movie, 3, self.price_code_new)
    self.assertEqual(rental.get_point(), 3.0)

    rental = Rental(self.children_movie, 10, self.price_code_children)
    self.assertEqual(rental.get_point(), 1.0)

    rental = Rental(self.regular_movie, 20, self.price_code_regular)
    self.assertEqual(rental.get_point(), 1.0)
