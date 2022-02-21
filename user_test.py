import unittest
from user import User

class TestUser(unittest.TestCase):

    def setUp(self):
        '''
        test runs before every test occurs
        '''
        self.new_user = User("Imelda", "wade", "0712345678", "test@user.com",)