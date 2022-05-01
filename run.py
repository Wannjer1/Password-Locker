from secrets import choice
import string 
from random import *
from tabnanny import check
from user import User
from credentials import Credentials


def create_user(username, email, password):
    '''function creates a new user'''

    new_user = User(username, email, password)
    return new_user

def save_user(user):
    '''function saves a new user'''
    user.save_user()

def delete_user(user):
    '''function deletes user account created'''
    user.delete_user()

def display_users():
    '''function displays existing user'''
    return User.display_users()

def login_user(username,password):
    '''function checks if a user exists and logs them in using their username and password'''
    check_user = User.verify_user(username, password)
    return check_user



#credentials
def create_useraccount(accountusername,accountemail,accountpassword):
    '''function creates new account'''
    new_account = Credentials(accountusername,accountemail,accountpassword)
    return new_account

def save_account(account):

    '''function saves credentials or account'''
    account.save_account(account)

def delete_account(account):
    '''function deletes saved credentials'''
    account.delete_account()

def display_accounts ():
    '''function displays all saved credentials'''
    return Credentials.display_accounts()

def find_cred (accountusername):
    '''function finds credentials '''
    return Credentials.find_cred(accountusername)

def check_account(accountemail):
    '''function checks if credentials exist'''
    return Credentials.if_account_exist(accountemail)

# def main ():
#     print("Welcome to pasword locker. To signup use ")
# input = input()

def main():
    print("Welcome to password locker")
    print("Enter one of the codes to proceed.\n CA --- Create New Account  \n LI --- log in to existing account")
    short_code = input("").lower().strip()
    if short_code == "ca":
        print("Sign Up")
        print('*' * 40)
        username = input("User_name: ")
        while True:
            print("TP - Type your password:\n ")
            choice = input().lower().strip()
            if choice == 'tp':
                password = input("Password\n")
                break
            else:
                print("Invalid password, please try again")
        save_user(create_user(username, password))
        print("*"*60)
        print(f"Hello {username}, your account has been created successfully. Your password is: {password}")
        print("*"*60)
    elif short_code == "li":
        print("*"*60)
        print("Enter your usernme and password to log in:")
        print("*"*60)
        username = input("User name: ")
        password = input("password: ")
        login = login_user(username, password)
        if login_user == login:
            print(f"Hi! {username}.Welcome to Password Locker")
            print("\n")
    
    while True:
        print("Use these short codes:\n CC -- Create a new account \n DC -- Display Credentials \n FC -- Find a credential \n GP -- Generate a random password \n D -- Delete credential \n EX -- Exit password locker \n")
        short_code = input().lower().strip()
        if short_code == "cc":
            print("Create New Credential")
            print("."*60)
            print("Account name ...")
            accountusername = input(). lower()
            print("Your Account username")
            username = input()
            while True:
                print("TP -- Type your own password if you already have an account :\n")
                choice = input().lower().strip()
                if choice == 'tp':
                    password = input ("Enter your password \n")
                    break
                else:
                    print("Invalid password please try again")
            save_account(create_useraccount(accountusername, username,password))
            print('\n')
            print(f"Account Credential for {accountusername}\n -- Username: {username}\n -- Password:{password}\n created successfully")
            print('\n')



        elif short_code == "dc":
            if display_accounts():
                print("Here's your list of your accounts: ")
                
                print('*' * 60)
                
                for account in display_accounts():
                    print(f" Account:{account.app_name} \n User Name:{account.user_name}\n Password:{account.password}")
                    
                print('*' * 60)
            else:
                print("You don't have any credentials saved yet..........")

        elif short_code == "fc":
            print("Enter the Account Name you want to search for")
            search_name = input().lower()
            if find_cred(search_name):
                search_credential = find_cred(search_name)
                print(f"Account Name : {search_credential.app_name}")
                print('-' * 60)
                print(f"User Name: {search_credential.user_name}\n Password :{search_credential.password}")
                print('-' * 60)
            else:
                print("That Credential does not exist")
                print('\n')
                
        elif short_code == "d":
            print("Enter the account name of the Credentials you want to delete")
            search_name = input().lower()
            if find_cred(search_name):
                search_credential = find_cred(search_name)
                print("*"*60)
                search_credential.delete_credentials()
                print('\n')
                print(f"Your stored credentials for : {search_credential.app_name} successfully deleted!!!")
                print('\n')
                print("*"*60)
            else:
                print("*"*60)
                print("That Credential you want to delete does not exist in your store yet")
                print("*"*60)


        elif short_code == 'ex':
            print("*"*60)
            print("Thanks for using passwordLocker.. bye!")
            print("*"*60)
            break
        else:
            print("Wrong entry... Try Again!")
    else:
        print("Please enter a valid input to continue")





if __name__ == '__main__':
    main()

     