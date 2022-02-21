class User:
    '''
     Class that generates new instances of users
    '''

    pass

    def __init__(self,first_name,last_name,phone_number,email):

        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email

user_list = []

def save_user(self):

    '''
    save_user method saves user objects into user_list
    '''

    User.user_list.append(self)

@classmethod
def find_by_nuber(cls,number):
    '''
    takes in a number and returns a user that matches number
    '''
    for user in cls.user_list:
        if user.phone_number == number:
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
