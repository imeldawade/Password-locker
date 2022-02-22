from user import User
from credential import Credential


def create_user(account, username, password):
    '''
    Function to create a new user
    '''
    new_user = User(account, username, password)
    return new_user

def save_user(user):
    User.save_user(user)

def delete_user(user):   
    User.delete_user(user)

def find_user(user):
    return User.find_by_username(user)

def check_existing_users(phone):
    return User.user_exist(phone)

def display_users():
    return User.display_users()

def create_site(site_name, password):
    credential = Credential(site_name, password)
    return credential

def save_site(user):
    Credential.save_site(user)

def find_site(sites ):
    return Credential.find_by_site(sites)

def check_existing_site(sites):
    return Credential.site_exists(sites)

def delete_site(user):
    Credential.delete_site(user)

def display_site():
    return Credential.display_site()

def main():
    print("Hello Welcome to your PASSWORD-LOCK. What is your name?")
    user_name = input()

    print(f"Hello {user_name}.")
    print('\n')

    while True:
            print("Use these numbers : 1 - create a new password, 2 - display passwords, 3 - Delete password, 4 -exit password list, 5- Login 2 ")

            numbers = input().lower()

            if numbers == '1':
                print("New Site")
                print("-"*10)

                print("Account")
                account = input()

                print ("User name ....")
                user_name = input()

                print("Password ...")
                password = input()

                save_site(create_user(account, user_name, password))
                print("Account created successfully")
                print("_"*10)
                print(f" Account:{account}\nUsername:{user_name}\nPassword:{password}")
                print("Login to your account")


                

            elif numbers == '2':

                if display_site():
                        print("Here is a list of your passwords")
                        print('\n')


            elif numbers == '3':
                print("Type the site you are deleting")

                site = input()
                if check_existing_site(site):
                    remove_site = (site)
                    delete_site(remove_site)

                else:
                    print(f'Invalid {site}')

            elif numbers == '4':
                print("Deleted")            

if __name__ == '__main__':
    main()




        






    
    