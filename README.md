# project-3-CLI

### PlumberMap

## By : Cindy Mutisya

# Date : 16/06/2024

# Description 
 This is a simple application where a user gets to access contacts of various plumbers and plumbers too get to login with their details so as to get a job from the users. This app displays the rate of a  plumber after services and it also enables one to book a plumber.

Database structure 
# Booking table
customer_id integer, foreign key from customers table
plumber_id integer, foreign key from plumbers table
date string

# customer table
customer_id integer, primary key 
name string
contact string

# Relationships
One-to-many relationship (between customer and plumber)
Many-to-many relationship (between plumber and the bookings)

# Functionality

Add Customers: Allows user to add new customers to the database, providing their personal details.
Add Plumbers: Enables user to add new plumbers to the system and other relevant information.
Add Booking: Allows user to add new bookings to the database and other pertinent information.
List Customers/Bookings/Plumbers: Provides functionality to view lists of Customers, Bookings, and Plumbers stored in the database.
Update Information: Allows users to update information in different tables, such as modifying customer details, booking details, or plumber contact information.
Delete Information: Allows users to delete records in different tables, such as removing customers, bookings, or plumbers.

# Usage
On running the application you will be presented with the following options
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
 
# example operation
1. Add customer 
     . Select option number 4 

2. Listing customers
     . Select option number 1

3.  Update customer
     . Select option number 7

4.  Delete customer
    . select option number 10

# Exiting
one clicks the option 16 to exit the application 

# Project set up instructions 
1. To access the project set up one can clone into this repository git clone git@github.com:Mutisya-Cindy/project-3-CLI.git.
2. Navigate to the directory.
3. Now the files are accessible to the project.

# Technologies used
The app uses Python, sqlite3 and CLI tools for interacting.

# Support and Contact details
github.com/Mutisya-Cindy.

# License
The content of this site is licensed under the MIT license Copyright (c) 2024.

# Video link for application
My app    ['https://drive.google.com/file/d/1-H4rXNzPTSEQCOgl8Y72puQLJN_bTc_j/view']




