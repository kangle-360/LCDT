#run.py
from  Database  import  *
from  Crypto  import  MD5crypto
from  SetStr  import  Strcompare

#modify
def ResetPassword ( username , oldpassword , newpassword , newagainpassword ):
    if username and oldpassword and newpassword and newagainpassword:
        passwordinDB = getvalueInRedis ( username )
        if  passwordinDB:
            md5oldpass = MD5crypto ( oldpassword )
            if Strcompare ( md5oldpass , passwordinDB ) and Strcompare ( newpassword , againpassword ):              
                updatepass = MD5crypto ( newpassword )
                if  setValueInRedis ( username , updatepass ):
                        return 1
    return 0

#register
def Register ( username , password , againpassword ):
    if username and password and againpassword:
        usernameinDB = getvalueInRedis ( username )
        if  usernameinDB == 0 and Strcompare ( password , againpassword ):
                MD5password = MD5crypto ( password )
                if  setValueInRedis ( username , MD5password ):           
                    return 1
    return 0