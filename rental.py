from movie import *
from pricecode import Pricecode
import logging
class Rental:
    """
	A rental of a movie by customer.
	From Fowler's refactoring example.
	A realistic Rental would have fields for the dates
	that the movie was rented and returned, from which the
	rental period is calculated.
	But for simplicity of the example only a days_rented
	field is used.
	"""

    def __init__(self, movie: Movie, days_rented, price_code: PriceCode):
        """Initialize a new movie rental object for
		   a movie with known rental period (daysRented).
		"""
        self.movie = movie
        self.days_rented = days_rented
        self.price_strategy = Pricecode.for_movie(self.movie)
        if not isinstance(self.price_strategy, Pricecode):
            log = logging.getLogger()
            log.error(
                f"Movie {self.movie.get_movie_title()} has unrecognized priceStrategy {self.movie}")

    def get_movie(self):
        return self.movie

    def get_days_rented(self):
        return self.days_rented

    def get_price(self):
        """compute rental change."""
        # return self.movie.get_price_code().price(self.days_rented)
        return self.price_code.price(self.days_rented)

    def get_point(self):
        """award renter points."""
        return self.price_code.points(self.days_rented)
