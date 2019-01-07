from exception_handling.userdefined import checkNumber
from exception_handling.userdefined import NumberTooBigError

try:
    num=int(input('enter number'))
    checkNumber(num)

except NumberTooBigError:
    print('enter a little small value')

