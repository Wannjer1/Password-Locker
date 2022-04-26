import pyperclip

class Credentials:
    """Class that generates new instances of credentials"""

    accounts=[]

    def __init__(self,accountusername,accountemail,accountpassword):
        """__init__method that helps us define properties for our objects self"""

        self.accountusername = accountusername
        self.accountemail = accountemail
        self.accountpassword = accountpassword

    def save_account(self):
        """save_account method saves user info into accounts"""

        Credentials.accounts.append(self)

    def delete_account(self):
        """delete_account method deletes a saved credential from accounts"""

        Credentials.accounts.remove(self)

    def display_accounts(cls):
        """method that returns a list of the accounts"""
        for  account in cls.accounts:
            return cls.accounts

    @classmethod
    def find_by_name(self, name):
        '''method that takes in a name and returns a credential'''

        for credentials in Credentials.accounts:
            if credentials.accountusername == name:
                return credentials



    # def find_by_number(cls,number):
    #     """method that takes in a number and returns a contact that matches that number"""

    #     for account in cls.accounts:
    #         if account.accountusername == number:
    #             return account