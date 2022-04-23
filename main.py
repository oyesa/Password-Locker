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
    Function to save a new user
    """
    user.save_user()