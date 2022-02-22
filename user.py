class User:
    '''
     Class that generates new instances of users
    '''

    user_list = []
    def __init__(self,account,username,password):

        self.account = account
        self.username = username
        self.password = password

    

    def save_user(self):

        '''
        save_user method saves user objects into user_list
        '''
        User.user_list.append(self)


    def delete_user(self):

        '''
        deletes a selected user
        '''
        User.user_list.remove(self)
            

    @classmethod
    def find_by_username(cls,username):
        '''
        takes in a number and returns a user that matches number
        '''
        for user in cls.user_list:
            if user.username == username:
                return user

    @classmethod
    def user_exist(cls,number):
        '''
        checks if a user exists from the user list
        '''
        for user in cls.user_list:
            if user.phone_number == number:
                return True

        return False 

    @classmethod
    def display_users(cls):
        '''
        returns the user list
        '''
        return cls.user_list
