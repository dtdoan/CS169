from django.test import TestCase
import unittest
from loginCount.models import UserModel

"""
Unit tests
"""

class TestUsers(unittest.TestCase):

    def setUp(self):
        self.users = UserModel()
        self.users.TESTAPI_resetFixture()

        
    def testAdd1(self):
        """
        Tests that adding a user works
        """
        self.assertEquals(UserModel.SUCCESS, self.users.add("user1", "password"))

    def testAddExists(self):
        """
        Tests that adding a duplicate user name fails
        """
        self.assertEquals(UserModel.SUCCESS, self.users.add("user1", "password"))
        self.assertEquals(UserModel.ERR_USER_EXISTS, self.users.add("user1", "password"))

    def testAdd2(self):
        """
        Tests that adding two users works
        """
        self.assertEquals(UserModel.SUCCESS, self.users.add("user1", "password"))
        self.assertEquals(UserModel.SUCCESS, self.users.add("user2", "password"))

    def testAddEmptyUsername(self): 
        """
        Tests that adding an user with empty username fails
        """
        self.assertEquals(UserModel.ERR_BAD_USERNAME, self.users.add("", "password"))


    '''
    def testAddUsername128long(self): 
        """
        Tests that adding an user with a username longer than 128 fails
        """
        self.assertEquals(UserModel.ERR_BAD_USERNAME, self.users.add("abcdefghijklmnopqrstuvwxyz
            abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxy",
            "password"))

    def testLoginSuccessful(self): 
        """
        Tests that logging in a user with correct password passes
        """
        self.assertEquals(UserModel.SUCCESS, self.users.login("user1", "password"))

    def testLoginUsernameNull(self): 
        """
        Tests that logging in a user not yet added to the database fails
        """
        self.assertEquals(UserModel.ERR_BAD_CREDENTIALS, self.users.login("user5", "password"))

    def testLoginBadCredentialCombination(self): 
        """
        Tests that logging in an user with the wrong password fails
        """
        self.assertEquals(UserModel.ERR_BAD_CREDENTIALS, self.users.login("user2", "badpassword"))

    def testLoginUsernameIsEmpty(self): 
        """
        Tests that logging in an user with empty username fails
        """
        self.assertEquals(UserModel.ERR_BAD_USERNAME, self.users.login("", "password"))

    def testLoginUsername128Long(self): 
        """
        Tests that logging in an user with too long a username fails
        """
        self.assertEquals(UserModel.ERR_BAD_USERNAME, self.users.login("abcdefghijklmnopqrstuvwxyz
            abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxy",
            "password"))

    def testLoginPasswordEmpty(self): 
        """
        Tests that logging in an user with empty password fails
        """
        self.assertEquals(UserModel.ERR_BAD_PASSWORD, self.users.login("user1", ""))

    def testLoginPassword128Long(self): 
        """
        Tests that logging in an user with a password too long fails
        """
        self.assertEquals(UserModel.ERR_BAD_PASSWORD, self.users.login("user1", "abcdefghijklmnopqrstuvwxyz
            abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxy"))

    def testAddandLogin(self): 
        """
        Tests that adding an user with empty username fails
        """
        self.assertEquals(UsersModel.SUCCESS, self.users.add("user10", "password10"))
        self.assertEquals(UsersModel.SUCCESS, self.users.login("user10", "password10"))

    def testLoginbeforeAdd(self): 
        """
        Tests that logging in before adding an user fails
        """
        self.assertEquals(UsersModel.ERR_BAD_CREDENTIALS, self.users.login("user10", "password10"))
        self.assertEquals(UsersModel.SUCCESS, self.users.add("user10", "password10"))
        '''


# If this file is invoked as a Python script, run the tests in this module
if __name__ == "__main__":
    # Add a verbose argument
    sys.argv = [sys.argv[0]] + ["-v"] + sys.argv[1:]
    unittest.main()
