from rental import Rental
from customer import Customer
from movie_catalog import MovieCatalog


def make_movie():
    catalog = MovieCatalog()
    movie = [
        catalog.get_movie("Mulan"),
        catalog.get_movie("No Time To Die"),
        catalog.get_movie("CitizenFour"),
        catalog.get_movie("Son of Saul")
    ]
    return movie


if __name__ == '__main__':
    # Create a customer with some rentals
    customer = Customer("Edward Snowden")
    catalog = MovieCatalog()
    days = 1
    for movie in make_movie():
        customer.add_rental(Rental(movie, days))
        days += 1
    print(customer.statement())