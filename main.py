import ast

from typing import List, Dict


def input_to_list(command_input: str) -> List:
    return command_input.split()


def check_admin_password(admin_password_dict: Dict, username: str, password: str) -> bool:
    try:
        if admin_password_dict[username] == password:
            return True
        return False
    except KeyError:
        return False


def check_user_password(user_password_dict: Dict, username: str, password: str) -> bool:
    try:
        if user_password_dict[username] == password:
            return True
        return False
    except KeyError:
        return False


def check_cart_list(cart: List, product_name: str) -> bool:
    for i in range(len(cart)):
        if product_name == cart[i][0]:
            cart[i][2] += 1
            return True
    return False


def check_user_account(user_password_dict: Dict, username: str) -> bool:
    for i in user_password_dict:
        if username == i:
            return False
    return True


def create_user_account(user_password_dict: Dict, username: str, password: str) -> None:
    if check_user_account(user_password_dict, username):
        user_password_dict[username] = password
        print(f"User {username} registered successfully. Please login now.")
    else:
        print(f"There is only one account with this {username}, choose another username")


def create_admin_account(admin_password_dict: Dict, username: str, password: str) -> None:
    admin_username = username
    admin_password = password
    admin_password_dict[admin_username] = admin_password


def calculate_total_price(cart: List) -> int:
    total_price = 0
    for product in cart:
        total_price += product[1] * product[2]
    return total_price


def print_catalog(catalog: Dict) -> None:
    for item, value in catalog.items():
        print(
            f"{item}: {value['Price']} - Stock: {value['Stock']}"
            f" - Description: {value['Description']}"
        )


def print_cart(cart: List) -> None:
    print("Shopping Cart Contents: ")
    total_price = 0
    for i in range(len(cart)):
        print(f"- {cart[i][0]}: {cart[i][2]}")
        total_price += cart[i][1] * cart[i][2]
    print(f"Total Price ${total_price}")


def print_orders(orders: Dict) -> None:
    print("Order History:")
    for user_name in orders:
        # print(orders)
        # print(user_name)
        print(
            f"User: {user_name} - Products: [{' '.join(orders[user_name]['Products'])}]"
            f" - Total: {orders[user_name]['Price']}"
        )


def add_to_cart(catalog: Dict, product_name: str, cart: List) -> None:
    try:
        product = catalog[product_name]
        if product["Stock"] > 0:
            if check_cart_list(cart, product_name):
                pass
            else:
                cart.append([product_name, product["Price"], 1])
            print(f"Product {product_name} added to the cart")
            catalog[product_name]["Stock"] -= 1
        else:
            print(f"Unfortunately, the {product_name} is out of stock.")
    except KeyError:
        print(f"There is no product called {product_name}")


def user_checkout(username: str, cart: List, orders: Dict) -> None:
    total_price = calculate_total_price(cart)
    orders[username] = {
        "Products": [product[0] + f"({product[2]})" for product in cart], "Price": total_price
    }
    print(f"Price {total_price} Payment successful. Order placed.")


def save_all_things(admin_password_dict: Dict, user_password_dict: Dict, catalog: Dict, order: Dict) -> None:
    with open("database.txt", "w") as file:
        file.write("Admin Passwords:\n")
        for key, value in admin_password_dict.items():
            file.write(f"{key}: {value}\n")

        file.write("\nUser Passwords:\n")
        for key, value in user_password_dict.items():
            file.write(f"{key}: {value}\n")

        file.write("\nCatalog:\n")
        for key, value in catalog.items():
            file.write(f"{key}: {value}\n")

        file.write("\nOrders:\n")
        for key, value in order.items():
            file.write(f"{key}: {value}\n")


def get_all_things() -> tuple[Dict, Dict, Dict, Dict]:
    admin_password_dict = {}
    user_password_dict = {}
    catalog = {}
    order = {}
    categories = {
        "Admin Passwords:": admin_password_dict,
        "User Passwords:": user_password_dict,
        "Catalog:": catalog,
        "Orders:": order
    }

    with open("database.txt", "r") as file:
        data = file.readlines()
        current_category = None
        for line in data:
            line = line.strip()
            if line in categories:
                current_category = line
            elif ":" in line and current_category:
                try:
                    key, value = line.split(": ", 1)
                    if value.startswith('{'):
                        value = ast.literal_eval(value)
                finally:
                    categories[current_category][key] = value
    print(admin_password_dict, user_password_dict, catalog, order)
    return admin_password_dict, user_password_dict, catalog, order


def admin_operations(admin_password_dict: Dict, user_password_dict: Dict, catalog: Dict, orders: Dict) -> None:
    print("Admin logged in successfully.")
    print("Admin logged in. You can use admin commands.")
    while True:
        command = input("Enter your command: ")
        command_list = command.split()
        try:
            if command_list[0] == "admin" and command_list[1] == "logout":
                break
            elif command_list[0] == "admin" and command_list[1] == "register":
                create_admin_account(admin_password_dict, command_list[2], command_list[3])
                print(f"Successfully added {command_list[2]} admin.")
            elif command_list[0] == "admin" and command_list[1] == "user_register":
                create_user_account(user_password_dict, command_list[2], command_list[3])
                print(f"Successfully added {command_list[2]} user.")
            elif command_list[0] == "admin" and command_list[1] == "update_product":
                catalog[command_list[2]] = {
                    "Price": command_list[3], "Stock": command_list[4], "Description": " ".join(command_list[5:])
                }
            elif command_list[0] == "admin" and command_list[1] == "view" and command_list[2] == "catalog":
                print_catalog(catalog)
            elif command_list[0] == "admin" and command_list[1] == "view" and command_list[2] == "orders":
                print_orders(orders)
            elif command_list[0] == "admin" and command_list[1] == "view" and command_list[2] == "usernames":
                for user in user_password_dict:
                    print(user)
            else:
                print("You typed wrong thing. Please try again...")
        except IndexError:
            print("You typed wrong thing. Please try again...")
    return


def user_operations(username: str, user_password_dict: Dict, catalog: Dict, orders: Dict) -> None:
    cart = []
    print(f"User {username} logged in successfully")
    print(f"User {username} logged in. You can use user commands.")
    while True:
        command = input("Enter your command: ")
        command_list = command.split()
        try:
            if command_list[0] == "user" and command_list[1] == "changepass":
                if user_password_dict[username] == command_list[2]:
                    user_password_dict[username] = command_list[3]
                    print(f"Password changed for user {username} successfully.")
                else:
                    print("You printed wrong password. Please try again!!!")
            elif command_list[0] == "user" and command_list[1] == "logout":
                if not any(cart):
                    print("User logged out successfully.")
                    break
                else:
                    answer = input("Your cart is not empty, Would you like to do a checkout? (Yes or no)")
                    if answer.lower() == "yes":
                        user_checkout(username, cart, orders)
                    print("User logged out successfully.")
                    break
            elif command_list[0] == "user" and command_list[1] == "add_to_cart":
                add_to_cart(catalog, command_list[2], cart)
            elif command_list[0] == "user" and command_list[1] == "checkout":
                user_checkout(username, cart, orders)
                cart = []
            elif command_list[0] == "user" and command_list[1] == "view" and command_list[2] == "catalog":
                print_catalog(catalog)
            elif command_list[0] == "user" and command_list[1] == "view" and command_list[2] == "cart":
                print_cart(cart)
                cart = []
            else:
                print("You typed wrong thing. Please try again...")
        except IndexError:
            print("You typed wrong thing. Please try again...")


def main():
    admin_password = {}
    user_password = {}
    catalog = {}
    orders = {}
    admin_password, user_password, catalog, orders = get_all_things()
    while True:
        print("""
        Please log in or create a new user account.
        Enter 'admin login <username> <password>' for admin login.
        Enter 'user login <username> <password>' for user login.
        Enter 'exit' to quit.
        """)
        command_input = input("Enter your command: ")
        input_list = input_to_list(command_input)
        if input_list[0] == "admin" and input_list[1] == "login":
            if check_user_password(admin_password, input_list[2], input_list[3]):
                admin_operations(admin_password, user_password, catalog, orders)
            else:
                print("Wrong username or password!!")
        elif input_list[0] == "user" and input_list[1] == "login":
            if check_user_password(user_password, input_list[2], input_list[3]):
                user_operations(input_list[2], user_password, catalog, orders)
            else:
                print("Wrong username or password!!")
        elif input_list[0] == "user" and input_list[1] == "register":
            create_user_account(user_password, input_list[2], input_list[3])
        elif input_list[0] == "exit":
            save_all_things(admin_password, user_password, catalog, orders)
            break
        else:
            print("You typed wrong thing. Please try again...")


if __name__ == "__main__":
    main()
