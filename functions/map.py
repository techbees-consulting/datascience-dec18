# map(function,sequence/iterable)

data = range(1,20,2)

def sq(list):
    list1=[]
    for i in list:
        list1.append(i*i)
    return list1

def sq1(n):
    return n*n

out=sq(data)
print(out)

l=list(map(sq1,data))
print(l)

map_lambda = list(map(lambda x:x*x,data))

print(map_lambda)
