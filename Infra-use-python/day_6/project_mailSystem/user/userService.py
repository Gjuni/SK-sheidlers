from config.mongodb import get_db
from user.userModel import generateCodeModel, sendmail, userPassword

def generateCode(email):
    code = generateCodeModel(email)
    sendmail(email, code)

    

def loginService(email, password):
    result = userPassword(email, password)

    return result