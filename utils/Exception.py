from rest_framework.exceptions import APIException

class MyException(APIException):
    def __init__(self, detail=None, code=None, error=None ,desc=None):
        super(MyException,self).__init__(detail,code)


