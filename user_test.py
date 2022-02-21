import unittest
from user import User

class TestUser(unittest.TestCase):

    def setUp(self):
        '''
        test runs before each test cases
        '''
        self.new_user = User("Imelda", "wade", "0712345678", "wade@user.com",)

    def test_init(self):
         '''
         test case to test if the object is initialized
         '''

         self.assertEqual(self.new_user.first_name,"Imelda")
         self.assertEqual(self.new_user.last_name,"Wade")
         self.assertEqual(self.new_user.phone_number,"0712345678")
         self.assertEqual(self.new_user.email,"wade@user.com")

    def test_save_user(self):
        '''
        test case to test if the save function works
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

    def test_save_multiple_user(self):
        '''
        test to check whether we saved multiple user objects to our user_list
        '''
        self.new_user.save_user()
        test_user = User("Test", "user","0712345678", "test@user.com")
        test_user.save_user()
        self.assertEqual(len(User.user_list)2)

    def tearDown(self):
        '''
        cleans up after each test case has run
        '''
        User.user_list = []

    def test_save_multiple_user(self):
        '''
        checks whether we can save multiple user objects to our user_list
        '''
        self.new_user.save_user()
        test_user = User("Test", "user", "0712345678", "test@user.com")
        test_user.save_user()
        self.assertEqual(len(User.user_list)2)
            
 

 