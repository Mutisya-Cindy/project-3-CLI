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

def list_bookings():
    bookings = Booking.all()
    for booking in bookings:
        print(f"Booking ID: {booking['id']}, Customer ID: {booking['customer_id']}, Plumber ID: {booking['plumber_id']}, Date: {booking['date']}, Time: {booking['time']}")

def add_customer():
    name = input("Name: ")
    email = input("Email: ")
    customer = Customer(name, email)
    customer.save()
    print(f"Customer {customer.name} added")       

def add_plumber():
    name = input("Name: ")
    rate = float(input("Rate: "))
    plumber = Plumber(name, rate)
    plumber.save()
    print(f"Plumber {plumber.name} added")

