from models.customer import Customer
from models.plumber import Plumber
from models.booking import Booking

def list_customers():
    customers = Customer.all()
    for customer in customers:
        print(f"Customer ID: {customer['id']}, Name: {customer['name']}, Email: {customer['email']}")

def list_plumbers():
    plumbers = Plumber.all()
    for plumber in plumbers:
        print(f"Plumber ID: {plumber['id']}, Name: {plumber['name']}, Rate: {plumber['rate']}")