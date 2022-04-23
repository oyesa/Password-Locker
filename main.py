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
