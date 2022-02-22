class Credential:
    

    user_credentials = []
    def __init__(self,page,pwd,User_name):
        self.page = page
        self.pwd = pwd
        self.username = User_name

    

    def save_site(self):
        '''
        
        '''
        Credential.user_credentials.append(self)
      