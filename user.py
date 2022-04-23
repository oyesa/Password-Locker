import string   #import string module for string manipulation
import random  #import random module to generate random numbers for password
import pyperclip  #import pyperclip module for copy and paste clipboard functions

class User:
    """
    Create User class and instantiate user
    """
    user_list = []

    def __init__(self, username, password):
        """
        method that defines the properties of a user.
        """
        self.username = username
        self.password = password

