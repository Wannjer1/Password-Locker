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
    def find_cred(cls,accountusername):
        """method to find users credentials/name"""

        for credentials in cls.accounts:
            if credentials.accountusername == accountusername:
                return credentials

    def cred_exist(cls,accountusername):
        """method to check if users credentials exist"""

        for credentials in cls.accounts:
            if credentials.accountusername == accountusername:
                return True
        return False



