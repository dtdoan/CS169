from django.db import models

class UserInfo(models.Model):
    username = models.CharField(max_length=128)
    password = models.CharField(max_length=128)
    count = models.IntegerField(default=1)

class UserModel(models.Model):
    ## The success return code
    SUCCESS               =   1
    ## Cannot find the user/password pair in the database (for login only)
    ERR_BAD_CREDENTIALS   =  -1
    ## trying to add a user that already exists (for add only)
    ERR_USER_EXISTS       =  -2
    ## invalid user name (empty or longer than MAX_USERNAME_LENGTH) (for add, or login)
    ERR_BAD_USERNAME      =  -3
    ## invalid password name (longer than MAX_PASSWORD_LENGTH) (for add)
    ERR_BAD_PASSWORD      =  -4
    ## The maximum length of user name
    MAX_USERNAME_LENGTH = 128
    ## The maximum length of the passwords
    MAX_PASSWORD_LENGTH = 128

    def login(self, username, password):
        if len(username) > self.MAX_USERNAME_LENGTH or len(username) == 0:
            return self.ERR_BAD_USERNAME
        if len(pwd) >= self.MAX_PASSWORD_LENGTH:
            return self.ERR_BAD_PASSWORD
        if UserInfo.objects.filter(username=username).exists():
            if UserInfo.objects.filter(username=username, password=pasword).exists():
                returning_user = UserInfo.objects.filter(username=username, password=password)[0]
                returning_user.count = returning_user.count + 1
                returning_user.save()
                return self.SUCCESS
            else:
                return self.ERR_BAD_CREDENTIALS
        else:
            return self.ERR_BAD_CREDENTIALS

    def add(self, usrn, pwd):
        if len(usrn) > self.MAX_USERNAME_LENGTH or len(usrn) == 0:
            return self.ERR_BAD_USERNAME
        if len(pwd) >= self.MAX_PASSWORD_LENGTH:
            return self.ERR_BAD_PASSWORD
        if UserInfo.objects.filter(username=usrn).exists():
            return self.ERR_USER_EXISTS
        user_added = UserInfo(username=usrn, password=pwd, count=1)
        new_user.save()
        return self.SUCCESS
        
    def __init__(self):
        pass       
    
    def __unicode__(self):
        return self.username

    # Used from constructor and self test
    def _reset(self):
        UserInfo.objects.all().delete()

    def TESTAPI_resetFixture(self):
        """
        This function is used only for testing, and should clear the database of all rows.

        It should always return SUCCESS (1)

        Used for testing
        """
        self._reset ()

