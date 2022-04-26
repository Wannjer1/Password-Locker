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