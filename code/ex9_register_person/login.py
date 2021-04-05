class Login:

    def __init__(self, user, password):
        self.__user = user
        self.__password = password
    
    def check(self, user, password):
        if self.__user == user and self.__password == password:
            print("Login successful")
            return True
        else:
            print("Enter a valid user and password")
            return False
