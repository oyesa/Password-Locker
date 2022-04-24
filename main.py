#!/usr/bin/env python3.8

from user import User
from user import Details

def create_new_user(username,password):

    """
    function to create a new user i.e. username and password
    """
    new_user = User(username,password)
    return new_user

def save_user(user):

    """
    function to save new user
    """
    user.save_user()
  
def display_user():

    """
    function to display existing user
    """
    return User.display_user()

def login_user(username,password):

    """
    function to check whether a user exist 
    """
    check_user = Details.verify_user(username,password)
    return check_user

def create_new_detail(account,userId,password):

    """
    function to create new details for a user account
    """
    new_detail = Details(account,userId,password)
    return new_detail

def save_detials(details):

    """
    function to save Details to details list
    """
    details. save_details()

def display_accounts_details():

    """
    function to return all the saved details
    """
    return Details.display_details()

def delete_detail(details):

    """
    function to delete Details from details list
    """
    details.delete_details()

def find_detail(account):

    """
    function to find user Details using account name 
    """
    return Details.find_detail(account)

def check_details(account):

    """
    function to check using account name, whether user Details exists(returns a boolean)
    """
    return Details.if_detail_exists(account)

def generate_Password():

    """
    function to generate password
    """
    auto_password = Details.generatePassword()
    return auto_password

def copy_password(account):

    """
    function to copy password using pyperclip module framework
    """
    return Details.copy_password(account)



def main():
    print("Hello Welcome to Password Locker 🙂...\n Please enter one of the shortcodes below to proceed.\n CNA ---  Create New Account  \n LI ---  Have An Existing Account  \n")

    short_code=input("").lower().strip()
    if short_code == "cna":
        print("Sign Up")
        print('*' * 85)

        username = input("User_name: ")

        while True:
            print(" TP - To type your own pasword:\n GP - To generate Password")
            password_Choice = input().lower().strip()

            if password_Choice == 'tp':
                password = input("Enter Password\n")
                break

            elif password_Choice == 'gp':
                password = generate_Password()
                break

            else:
                print("Invalid password! Try again")

        save_user(create_new_user(username, password))
        print("*"*85)
        print(f"Hello {username} 🙂, Your account has been created succesfully! Your password is: {password}")
        print("*"*85)

    elif short_code == "li":
        print("*"*85)
        print("Enter your username and Password to login:")
        print('*' * 85)
        username = input("Username: ")
        password = input("Password: ")
        login = login_user(username,password)
        if login_user == login:
            print(f"Hello {username} 🙂 Welcome Back!")  
            print('\n')

    while True:
        print("Use these short codes to navigate Password Locker:\n CND - Create New Details \n DD - Display Details \n FD - Find a Detail \n GRP - Generate Random Password \n D - Delete Detail \n EX - Exit Application \n")
        short_code = input().lower().strip()

        if short_code == "cnd":
            print("Create New Details")
            print("."*20)
            print("Account name ....")
            account = input().lower()
            print("Your Account username")
            userId = input()
            while True:
                print(" IP - To input own pasword if you have an existing account:\n GRP - To generate random password")
                password_Choice = input().lower().strip()
                if password_Choice == 'ip':
                    password = input("Enter Your Own Password\n")
                    break

                elif password_Choice == 'grp':
                    password = generate_Password()
                    break

                else:
                    print("Invalid password! Please try again")

            save_details(create_new_detail(account,userId,password))
            print('\n')
            print(f"Account Detail for: {account} - UserId: {userId} - Password:{password} created succesfully")
            print('\n')
        elif short_code == "dd":
            if display_accounts_details():
                print("Here's your list of acoounts: ")
                print('*' * 30)
                print('_'* 30)

                for account in display_accounts_details():
                    print(f" Account:{account.account} \n User Name:{username}\n Password:{password}")
                    print('_'* 30)
                print('*' * 30)
            else:
                print("You don't have any saved details yet.")
        elif short_code == "fd":
            print("Enter the Account Name you want to search for.")
            search_name = input().lower()
            if find_detail(search_name):
                search_detail = find_detail(search_name)
                print(f"Account Name : {search_detail.account}")
                print('-' * 50)
                print(f"User Name: {search_detail.userId} Password :{search_detail.password}")
                print('-' * 50)


