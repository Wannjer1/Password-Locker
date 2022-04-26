import random 
import string

from requests import delete 

class User:
    """Created class that generates new instances of users"""

    userslist = []
    def __init__(self,username,email,password):
        """__init__ method that helps define properties for our object self
        
        Args:
            username: to identify user
            email: to check user email
            password: a password for the user account"""

        self.username = username
        self.email = email
        self.password = password

    def save_user(self):
        """save_user method that saves user info into the user userlist"""
        User.userslist.append(self)

    def delete_user(self):
        """delete_user method that deletes a saved user from the userlist"""
        User.userslist.remove(self)