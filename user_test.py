import unittest
from user import User

class Testuser (unittest.TestCase):
    """Test class that defines test cases for the user class behavours
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases"""

    def setUp(self):
        '''set up method to run before each test case'''
        self.new_user = User("Ann", "annie@gmail.com", "#pass123")

    def  test_init(self):
        '''test_init method to test if the object is initialised properly'''
        self.assertEqual(self.new_user.username,"Ann")
        self.assertEqual(self.new_user.password,"#pass123")

    def test_save_user(self):
        '''test_save_user test case to test if the user object is saved into the user list'''

        self.new_user.save_user() #saves new contact
        self.assertEqual(len(User.user_list),1)

    def test_delete_user(self):
        '''test_delete_contact to test if we can remove a user name from the user list'''
        self.new_contact.save_contact()
        test_user = User("Test","user","0792940900","test@user.com")
        test_user.save_user()

        self.new_user.delete_user()#deletes a contact object
        self.assertEqual(len(User.user_list),1)
    

if __name__ == '__main__':
    unittest.main()