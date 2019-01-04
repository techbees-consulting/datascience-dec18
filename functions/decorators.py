def decor(fun):
     def inner():
        value = fun()
        return value*3
     return inner

def decor1(fun):
     def inner():
        value = fun()
        return value+2
     return inner

@decor
def display():
    return 10

@decor1
@decor
def display1():
    return 20
print(display())
print(display1())
