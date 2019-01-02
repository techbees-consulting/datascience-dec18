#fact 4*3*2*1 1-1
#fibonocci

def fact(n):
    if n==0:
        result =1
    else:
        result = n*fact(n-1)
    return result

#5*fact(4)->4*fact(3)->1


# print(fact(5))


def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

print(fib(10))

