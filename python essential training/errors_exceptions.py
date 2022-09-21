from logging import raiseExceptions
import time

#FINALLY
def causeError():
    start = time.time()
    try:
        time.sleep(0.5) #pause the execution the amount of seconds specified
        1/0
    except Exception as e: #e is going to be our variable, actually is the instance of the exception that was raised.
        print('There was some sort of error')
    finally:
        print(f'Function took {time.time() - start} seconds to execute') #This will always execute even is there no exception

#causeError()

#CATCHING EXCEPTIONS BY TYPE

def causeError():
    start = time.time()
    try:
        x = 1 + 'a'
    except TypeError:
        print('There was a type error')
    except ZeroDivisionError:
        print('There was a zero division error')
    except Exception as e: #e is going to be our variable, actually is the instance of the exception that was raised.
        print('There was some sort of error')
    finally:
        print(f'Function took {time.time() - start} seconds to execute') #This will always execute even is there no exception

#causeError()

#CUSTOM DECORATORS

def handleException(func):
    def wrapper(*args):
        try:
            func(*args)
        except TypeError:
            print('There was a type error')
        except ZeroDivisionError:
            print('There was a zero division error')
        except Exception as e: #e is going to be our variable, actually is the instance of the exception that was raised.
            print('There was some sort of error')

    return wrapper

@handleException
def causeError():
    return 1/0

causeError()

#RAISING EXCEPTIONS

@handleException
def raiseError(n):
   if n == 0:
       raise Exception
   print(n)

raiseError(0) #print There was some sort of error
raiseError(1) #print 1