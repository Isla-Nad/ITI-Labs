import re
import json


def validate_phone_number(phone_number):
    pattern = r'^01[0-2]\d{8}$'
    return re.match(pattern, phone_number)


def load_user_data():
    try:
        with open('users.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def save_user_data(data):
    user_db = load_user_data()
    user_db.update(data)
    with open('users.json', 'w') as file:
        json.dump(user_db, file, indent=4)


def register_user():
    print("User Registration")
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    confirm_password = input("Confirm your password: ")
    mobile_phone = input("Enter your mobile phone number: ")

    if password != confirm_password:
        print('\033[91m'+"Passwords do not match. Registration failed."+'\033[0m')
        return

    if not validate_phone_number(mobile_phone):
        print(
            '\033[91m'+"Invalid mobile phone number. Registration failed."+'\033[0m')
        return

    user_db = load_user_data()

    if email in user_db:
        print(
            '\033[91m'+"User with this email already exists. Registration failed."+'\033[0m')
        return

    user_db[email] = {
        'first_name': first_name,
        'last_name': last_name,
        'password': password,
        'mobile_phone': mobile_phone,
        'activated': False
    }

    save_user_data(user_db)

    print(
        '\033[92m'+"Registration successful."+'\033[92m')


def login_user():
    print("User Login")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    user_db = load_user_data()

    if email in user_db and user_db[email]['password'] == password:
        print('\033[92m'+"Login successful. Welcome, {}!".format(
            user_db[email]['first_name'])+'\033[0m')
        return email
    else:
        print(
            '\033[91m'+"Login failed. Please check your email, password."+'\033[0m')
