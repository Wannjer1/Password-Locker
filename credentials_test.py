import unittest
from credentials import Credentials


class TestCredentials(unittest.TestCase):
    def setUp(self):
        self.new_account = Credentials("Ann","annie@gmail.com","#pass123")

    def tearDown(self):
        Credentials.accounts = []

    def test_init(self):
        self.assertEqual(self.new_account.accountusername,"Ann")
        self.assertEqual(self.new_account.accountemail,"annie@gmail.com")
        self.assertEqual(self.new_account.accountpassword,"#pass123")

    def test_save_user(self):
        '''Tests is a new credential has been created and saved'''
        self.new_account.save_account()
        self.assertEqual(len(Credentials.accounts),1)

    def test_delete_user(self):
        """test_delete_user method to enable users to delete accounts"""

        self.new_account.save_account()
        test_account = Credentials("Ann", "annie@gmail.com","#pass123")
        test_account.save_account()
        self.new_account.delete_account()
        self.assertEqual(len(Credentials.accounts),1)

    def test_account_exist(self):
        '''test to identify whether a user account or credential exists'''

        self.new_account.save_account()
        the_account = Credentials("Ann", "annie@gmail.com", "#pass123")
        the_account.save_account()
        account_is_found = Credentials.if_account_exist("annie@gmail.com")
        self.assertTrue(account_is_found)


    def test_display_user(self):
        self.assertEqual(Credentials.display_accounts(),Credentials.accounts)


    if __name__ == '__main__':
        unittest.main()