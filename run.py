from user import User

def create_user(fname, lname, phone, email):
    '''
    Function to create a new user
    '''
    new_user = User(fname, lname, phone, email)
    return new_user

def save_users(user):
    '''
    Function to save user
    '''
    user.save_user()

def del_user(user):
    '''
    Function to delete a user
    '''        
    user.delete_user()

def find_user(user):
    '''
    Functions that takes in a number and calls the user class method
    '''    
    return User.find_by_number(number)

def check_existing_users(number):
    '''
    Function that checks if a user exists with that number
    '''    
    return User.user_exist(number)
    

    
    