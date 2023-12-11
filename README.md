# Online Store System

## Overview

The project aims to simulate an online store environment where users can interact through a command-line interface. Users can perform various actions, such as registering, logging in, changing passwords, browsing products, adding items to their carts, checking out, and viewing order history.

## Functionality

The key functionalities provided by this system include:
- **User Authentication:** Users can register with a username and password, and existing users can log in securely.
- **User Operations:** Once logged in, users can change their passwords, view the product catalog, add products to their shopping carts, view their carts, and make payments.
- **Admin Operations:** Admins have additional functionalities like viewing the product catalog, updating product information, viewing user orders, and accessing usernames.

## Purpose

The primary goal of this project was to enhance Python programming skills while focusing on basic data manipulation within fundamental iterable data types. The project aimed to achieve the following:
- Strengthen understanding of Python programming concepts and syntax.
- Practice utilizing dictionaries and lists for storing and manipulating data.
- Implement command-line interaction and basic user authentication functionalities.


## Usage

To run the project, follow these steps:

1. **User Operations:**
    - Logging in as user:
     ```
     user login <username> <password>
     ```
   - Changing the password:
     ```
     user changepass <old password> <new password>
     ```
   - Viewing the product catalog:
     ```
     user view catalog
     ```
   - Adding a product to the shopping cart:
     ```
     user add to cart <product name>
     ```
   - Viewing the shopping cart:
     ```
     user view cart
     ```
   - Making a payment:
     ```
     user checkout
     ```
     - Logging out of the account:
     ```
     user logout
     ```

2. **Admin Operations:**
   - Logging in as an admin:
     ```
     admin login <username> <password>
     ```
   - Viewing the product catalog:
     ```
     admin view catalog
     ```
   - Updating product information:
     ```
     admin update product <product name> <price> <stock> <description>
     ```
   - Viewing orders:
     ```
     admin view orders
     ```
   - Viewing usernames:
     ```
     admin view usernames
     ```
   - Logging out of the account:
     ```
     admin logout
     ```

## Contribution

Contributions to this project are welcome. Feel free to fork the repository, make improvements, and create a pull request with your changes.

## Project Purpose

The purpose of this project was to enhance my Python skills and learn basic data manipulation in fundamental iterable data types. Through this project, I aimed to improve my understanding of Python programming by implementing a command-line online store system.
