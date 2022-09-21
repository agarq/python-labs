class CustomException(Exception):
    pass

def causeError():
    raise CustomException('You called the causeError() function')

#causeError()

#ADDING ATTRIBUTES
class HttpException(Exception):
    statusCode = None
    message = None

    def __init__(self):
        super().__init__(f'Status code:  {self.statusCode} and message is: {self.message}')

class NotFound(HttpException):
    statusCode = 404
    message = 'Resource not found'

class ServerError(HttpException):
    statusCode = 500
    message = 'This server messed up !'

def raiseServerError():
    raise ServerError()

raiseServerError()