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

def book_plumber():
    customer_id = int(input("Customer ID: "))
    plumber_id = int(input("Plumber ID: "))
    date = input("Date: ")
    booking = Booking(customer_id, plumber_id, date)
    booking.save()
    print(f"Booking {booking.date} added")    


def update_customer():
    customer_id = int(input("Customer ID: "))
    name = input("Name: ")
    email = input("Email: ")
    Customer.update(customer_id, name, email)
    print(f"Customer {customer_id} updated")

def update_plumber():
    plumber_id = int(input("Plumber ID: "))
    name = input("Name: ")
    rate = float(input("Rate: "))
    Plumber.update(plumber_id, name, rate)
    print(f"Plumber {plumber_id} updated")

def update_bookings():
    booking_id = int(input("Booking ID: "))
    customer_id = int(input("Customer ID: "))
    plumber_id = int(input("Plumber ID: "))
    date = input("Date: ")
    Booking.update(booking_id, customer_id, plumber_id, date)
    print(f"Booking {booking_id} updated")


def delete_customer():
    customer_id = int(input("Customer ID: "))
    Customer.delete(customer_id)
    print(f"Customer {customer_id} deleted")

def delete_plumber():
    plumber_id = int(input("Plumber ID: "))
    Plumber.delete(plumber_id)
    print(f"Plumber {plumber_id} deleted")

def delete_bookings():
    booking_id = int(input("Booking ID: "))
    Booking.delete(booking_id)
    print(f"Booking {booking_id} deleted")