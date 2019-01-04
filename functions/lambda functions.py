#function with no name
g = lambda n:n*n

print(g(12))

def func(x,y):
    sum = x+y
    return sum

f = lambda x,y:x+y

print(f(10,11))

def func1(x,y):
    if x>y:
        return x
    else:
        return y

h = lambda x,y: x if x>y else y

print(h(33,25))
