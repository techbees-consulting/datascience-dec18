#!python
# define your own exceptions
class NumberTooSmallError(Exception):pass

class NumberTooBigError(Exception):
    print('\nException: NumberTooBigError:\nYour number is too big. \nTry a smaller one!')

class NumberThreeError(Exception):

        print ('\nException: ThreeNumberError:\nThree is not number ya\'re lookin\' for.\n')

class NumberFiveError(Exception):pass #uncaught exception


#function that uses user-defined exceptions
def checkNumber(num):
    if(num == 3):
        raise NumberThreeError
    elif(num == 5):
        raise NumberFiveError
    elif(num < 99):
        raise NumberTooSmallError
    elif(num > 99):
        raise NumberTooBigError
    return num


