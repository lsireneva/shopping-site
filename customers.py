"""Customers at Hackbright."""


class Customer:
    """Ubermelon customer."""

    def __init__(self, name, username, email, password):
        self.name = name
        self.username = username
        self.email = email
        self.password = password

def read_customers_from_file(filepath):
    customers = {}
    
    with open(filepath) as file:
        for line in file:
            (name, username, email, password) = line.strip().split("|")

            customers[email] = Customer(name, username, email, password)
    return customers


def get_by_email(email):

    return customers[email]

customers = read_customers_from_file("customers.txt")
