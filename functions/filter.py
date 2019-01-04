#accepts function and sequence as inputs

def is_even(x):
    if (x%2)==0:
        return True
    else:
        return False

data = range(1,10)
list = [33,22,11,54,9]
# dict = [{'name':'a','loc':b},{},{}..]

even_data = filter(is_even,data)
even_lambda = filter(lambda x:(x%2)==0,list)


print(even_data)
print(even_lambda)

