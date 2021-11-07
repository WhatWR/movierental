from enum import Enum
import pandas
from datetime import date


class MovieCatalog:
    """Factory for Movie."""

    def __init__(self):
        self.movies = []
        with open("movies.csv", "r", newline="") as csv_file:
            csv_reader = csv.reader(csv_file)
            list_of_rows = list(csv_reader)
            for row in range(1, len(list_of_rows)):
                collect_title = list_of_rows[row][1]
                collect_year = list_of_rows[row][2]
                collect_genre = list_of_rows[row][3].split("|")
                self.movies.append(Movie(collect_title, collect_year, collect_genre))

    def get_movie(self, title: str):
        """Returns a movie with matching title."""
        for movie in self.movies:
            if title == movie.get_title():
                return movie

class Movie:
	"""
	A movie available for rent.
	"""
	
	def __init__(self, title, year, genre):
		# Initialize a new movie. 
		self.__title = title
		self.__year = year
		self.__genre = genre

	def is_genre(self, string):
		"""returns true if the string parameter matches one of the movie’s genre."""
		if string in self.__genre:
			return True
		return False

	def get_year(self):
		return self.__year
	
	def get_title(self):
		return self.__title

	def get_genre(self):
		return self.__genre
	
	def __str__(self):
		return self.__title


class PriceCode(Enum):
	"""An enumeration for different kinds of movies and their behavior"""
	NEW_RELEASE = { "price": lambda days: 3.0*days, 
					"frp": lambda days: days
					}
	REGULAR = { "price": lambda days: 2 if days <= 2 else 2 + 1.5*(days-2),
				"frp": lambda days: 1
				}
	CHILDREN = {"price": lambda days: 1.5 if days <= 3 else 1.5 + 1.5*(days-3),
				"frp": lambda days: 1
				}

	def price(self, days: int) -> float:
		"Return the rental price for a given number of days"""
		pricing = self.value["price"]    # the enum member's price formula
		return pricing(days)

	def points(self, days: int) -> float:
		"""Return the rental points for a given of days of new release movie or regular movie."""
		point = self.value["frp"]
		return point(days)

	def for_movie(movie: Movie):
		"""Figure the price which depend on the genre and release date."""
		if movie.get_year() == str(date.today().year):
			return PriceCode.NEW_RELEASE
		elif 'Children' in movie.get_genre():
			return PriceCode.CHILDREN
		return PriceCode.REGULAR