from user import User
from credential import Credential
import unittest

class TestUser(unittest.TestCase):
    def tearDown(self):
        '''
        cleans up after each test case has run
        '''
        User.user_list = []

    def setUp(self):
        '''
        test runs before each test cases
        '''
        self.new_user = User("Email", "Imelda", "imelda01")

    def test_init(self):
         '''
         test case to test if the object is initialized
         '''

         self.assertEqual(self.new_user.account,"Email")
         self.assertEqual(self.new_user.username,"Imelda")
         self.assertEqual(self.new_user.password, "imelda01")

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
        test_user = User("Email", "Imelda", "imelda01")
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)


    def test_save_multiple_user(self):
        '''
        checks whether we can save multiple user objects to our user_list
        '''
        self.new_user.save_user()
        test_user = User("account", "username", "password",)
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)

    def test_delete_user(self):
        '''
        test that checks the delete function
        '''
        self.new_user.save_user()
        test_user = User("Email", "Imelda", "imelda01")
        test_user.save_user()

        self.new_user.delete_user()
        self.assertEqual(len(User.user_list),1)

    def delete_user(self):
        '''
        deletes a saved user from the user_list
        '''

        User.user_list.remove(self)

    def test_find_user_by_number(self):
        '''
        checks if we can find user by phone number and display information
        '''

        self.new_user.save_user()
        test_user = User("Email", "Imelda", "imelda01")
        test_user.save_user()


        found_user = User.find_by_number("0111222333")
        self.assertEqual(found_user.email,test_user.email)

    # def test_user_exists(self):
    #     '''
    #     checks if a user exists from the user_list
    #     '''
    #     for user in cls.user_list:
    #         if user.phone_number == number:
    #             return True

    #     return False

    def test_display_all_user(self):
        '''
        returns a list of all users saved
        '''
        self.assertEqual(User.display_users(),User.user_list)

if __name__ == '__main__':
    unittest.main()

