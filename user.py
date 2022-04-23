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
        instantiate user properties
        """
        self.username = username
        self.password = password

    def save_user(self):

        """
        method to saves new user to user list
        """
        User.user_list.append(self)

    @classmethod
    def display_user(cls):
        return cls.user_list

    def delete_user(self):

        """
        method to delete a  saved account from the user_list
        """
        User.user_list.remove(self)    

