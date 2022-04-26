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
        self.new_account.save_account()
        self.assertEqual(len(Credentials.accounts),1)

    def test_delete_user(self):
        """test_delete_user method to enable users to delete accounts"""

        self.new_account.save_account()
        test_account = Credentials("Ann", "annie@gmail.com","#pass123")
        test_account.save_account()
        self.new_account.delete_account()
        self.assertEqual(len(Credentials.accounts),1)


    def test_display_user(self):
        self.assertEqual(Credentials.display_accounts(),Credentials.accounts)


    if __name__ == '__main__':
        unittest.main()