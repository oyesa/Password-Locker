#!/usr/bin/env python3.8

from user import User, Details

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

def delete_credential(details):

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

