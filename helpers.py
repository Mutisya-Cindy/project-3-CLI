from models.customer import Customer
from models.plumber import Plumber
from models.booking import Booking

def list_customers():
    customers = Customer.all()
    for customer in customers:
        print(f"Customer ID: {customer['id']}, Name: {customer['name']}, Contact: {customer['contact']}")

def list_plumbers():
    plumbers = Plumber.all()
    for plumber in plumbers:
        print(f"Plumber ID: {plumber['id']}, Name: {plumber['name']}, Rate: {plumber['rate']}")

def list_bookings():
    bookings = Booking.all()
    for booking in bookings:
        print(f"Booking ID: {booking['id']}, Customer: {booking['customer_name']}, Plumber: {booking['plumber_name']}, Date: {booking['date']}")

def add_customer():
    name = input("Enter customer name: ")
    contact = input("Enter customer contact: ")
    customer = Customer(name, contact)
    customer.save()
    print(f"Customer {name} added.")

def add_plumber():
    name = input("Enter plumber name: ")
    rate = float(input("Enter plumber rate: "))
    plumber = Plumber(name, rate)
    plumber.save()
    print(f"Plumber {name} added.")

def book_plumber():
    customer_id = int(input("Enter customer ID: "))
    plumber_id = int(input("Enter plumber ID: "))
    date = input("Enter booking date (YYYY-MM-DD): ")
    booking = Booking(customer_id, plumber_id, date)
    booking.save()
    print(f"Booking for customer {customer_id} with plumber {plumber_id} on {date} added.")

def update_customer():
    customer_id = int(input("Enter customer ID: "))
    name = input("Enter new customer name: ")
    contact = input("Enter new customer contact: ")
    Customer.update(customer_id, name, contact)
    print(f"Customer {customer_id} updated.")

def update_plumber():
    plumber_id = int(input("Enter plumber ID: "))
    name = input("Enter new plumber name: ")
    rate = float(input("Enter new plumber rate: "))
    Plumber.update(plumber_id, name, rate)
    print(f"Plumber {plumber_id} updated.")

def update_booking():
    booking_id = int(input("Enter booking ID: "))
    customer_id = int(input("Enter new customer ID: "))
    plumber_id = int(input("Enter new plumber ID: "))
    date = input("Enter new booking date (YYYY-MM-DD): ")
    Booking.update(booking_id, customer_id, plumber_id, date)
    print(f"Booking {booking_id} updated.")

def delete_customer():
    customer_id = int(input("Enter customer ID to delete: "))
    Customer.delete(customer_id)
    print(f"Customer {customer_id} deleted.")

def delete_plumber():
    plumber_id = int(input("Enter plumber ID to delete: "))
    Plumber.delete(plumber_id)
    print(f"Plumber {plumber_id} deleted.")

def delete_booking():
    booking_id = int(input("Enter booking ID to delete: "))
    Booking.delete(booking_id)
    print(f"Booking {booking_id} deleted.")

def search_customers():
    search_term = input("Enter customer name to search: ")
    customers = Customer.search(search_term)
    for customer in customers:
        print(f"Customer ID: {customer['id']}, Name: {customer['name']}, Contact: {customer['contact']}")

def search_plumbers():
    search_term = input("Enter plumber name to search: ")
    plumbers = Plumber.search(search_term)
    for plumber in plumbers:
        print(f"Plumber ID: {plumber['id']}, Name: {plumber['name']}, Rate: {plumber['rate']}")

def search_bookings():
    search_term = input("Enter booking ID to search: ")
    bookings = Booking.search(search_term)
    for booking in bookings:
        print(f"Booking ID: {booking['id']}, Customer: {booking['customer_name']}, Plumber: {booking['plumber_name']}, Date: {booking['date']}")