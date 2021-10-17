from rental import Rental
from pricecode import PriceCode
import logging

from enum import Enum


class PriceCode(Enum):
    """An enumeration for different kinds of movies and their behavior"""
    new_release = {"price": lambda days: 3.0 * days,
                   "frp": lambda days: days
                   }
    normal = {"price": lambda days: 1.5 * days + 2.0 if (days > 2) else 2.0,
              "frp": lambda days: 1
              }
    childrens = {"price": lambda days: 1.5 * days + 2.5 if (days > 3) else 1.5,
                 "frp": lambda days: 1
                 }

    def price(self, days: int) -> float:
        "Return the rental price for a given number of days"""
        pricing = self.value["price"]  # the enum member's price formula
        return pricing(days)


class Customer:
    """
       A customer who rents movies.
       The customer object holds information about the
       movies rented for the current billing period,
       and can print a statement of his rentals.
    """

    def __init__(self, name: str):
        """ Initialize a new customer."""
        self.name = name
        self.rentals = []

    def add_rental(self, rental: Rental):
        if rental not in self.rentals:
            self.rentals.append(rental)

    def get_name(self):
        return self.name

    def statement(self):
        """
            Print all the rentals in current period, 
            along with total charges and reward points.
            Returns:
                the statement as a String
        """
        total_amount = 0  # total charges
        frequent_renter_points = 0
        statement = f"Rental Report for {self.name}\n\n"
        fmt = "{:32s}    {:4s} {:6s}\n"
        statement += fmt.format("Movie Title", "Days", "Price")
        fmt = "{:32s}   {:4d} {:6.2f}\n"

        for rental in self.rentals:
            # compute rental change
            amount = 0
            if rental.get_movie().get_price_code() == PriceCode.normal:
                # Two days for $2, additional days 1.50 each.
                amount = 2.0
                if rental.get_days_rented() > 2:
                    amount += 1.5 * (rental.get_days_rented() - 2)
            elif rental.get_movie().get_price_code() == PriceCode.childrens:
                # Three days for $1.50, additional days 1.50 each.
                amount = 1.5
                if rental.get_days_rented() > 3:
                    amount += 1.5 * (rental.get_days_rented() - 3)
            elif rental.get_movie().get_price_code() == PriceCode.new_release:
                # Straight per day charge
                amount = 3 * rental.get_days_rented()
            else:
                log = logging.getLogger()
                log.error(
                    f"Movie {rental.get_movie()} has unrecognized priceCode {rental.get_movie().get_price_code()}")
            # award renter points
            if rental.get_movie().get_price_code() == PriceCode.new_release:
                frequent_renter_points += rental.get_days_rented()
            else:
                frequent_renter_points += 1
            #  add detail line to statement
            statement += fmt.format(rental.get_movie().get_title(), rental.get_days_rented(), amount)
            # and accumulate activity
            total_amount += amount

        # footer: summary of charges
        statement += "\n"
        statement += "{:32s} {:6s} {:6.2f}\n".format(
            "Total Charges", "", total_amount)
        statement += "Frequent Renter Points earned: {}\n".format(frequent_renter_points)

        return statement


if __name__ == "__main__":
    customer = Customer("Edward Snowden")
    print(customer.statement())
    movie = PriceCode("Hacker Noon", PriceCode.normal)
    customer.add_rental(Rental(movie, 2))
    movie = PriceCode("CitizenFour", PriceCode.new_release)
    customer.add_rental(Rental(movie, 3))
    print(customer.statement())
