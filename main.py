# Demonstrate the movie rental code.
# Create a customer with some movies and print a statement.

from pricecode import PriceCode
from rental import Rental
from customer import Customer

def make_movies():
    movies = [
        PriceCode("The Irishman", PriceCode.new_release),
        PriceCode("CitizenFour", PriceCode.normal),
        PriceCode("Frozen", PriceCode.childrens),
        PriceCode("El Camino", PriceCode.new_release),
        PriceCode("Particle Fever", PriceCode.normal)
    ]
    return movies


if __name__ == '__main__':
    # Create a customer with some rentals
    customer = Customer("Edward Snowden")
    days = 1
    for movie in make_movies():
        customer.add_rental(Rental(movie, days))
        days += 1
    print(customer.statement())
