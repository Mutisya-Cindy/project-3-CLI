from database.setup import create_tables
from helpers import (
    list_customers, list_plumbers, list_bookings,
    add_customer, add_plumber, book_plumber,
    update_customer, update_plumber, update_booking,
    delete_customer, delete_plumber, delete_booking,
    search_customers, search_plumbers, search_bookings
)

def main():
    create_tables()  

    while True:
        print("""
        1. List customers
        2. List plumbers
        3. List bookings
        4. Add customer
        5. Add plumber
        6. Book plumber
        7. Update customer
        8. Update plumber
        9. Update booking
        10. Delete customer
        11. Delete plumber
        12. Delete booking
        13. Search customers
        14. Search plumbers
        15. Search bookings
        16. Exit
        """)

        choice = input("Enter your choice: ")

        if choice == '1':
            list_customers()
        elif choice == '2':
            list_plumbers()
        elif choice == '3':
            list_bookings()
        elif choice == '4':
            add_customer()
        elif choice == '5':
            add_plumber()
        elif choice == '6':
            book_plumber()
        elif choice == '7':
            update_customer()
        elif choice == '8':
            update_plumber()
        elif choice == '9':
            update_booking()
        elif choice == '10':
            delete_customer()
        elif choice == '11':
            delete_plumber()
        elif choice == '12':
            delete_booking()
        elif choice == '13':
            search_customers()
        elif choice == '14':
            search_plumbers()
        elif choice == '15':
            search_bookings()
        elif choice == '16':
            print("Goodbye, thanks for using the Plumber Booking App!")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
