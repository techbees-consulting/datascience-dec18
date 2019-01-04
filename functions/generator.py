#generator(inputs args)

def myrange(x,y):
    while x<=y:
        yield x
        x+=1

r = myrange(10,20)

# for i in r:
#     print(i)

# print(next(r))
# print(next(r))
# print(next(r))
# print(next(r))

def gen():
    yield 'A'
    yield 'B'
    yield 'C'

g=gen()
for i in g:
    print(i)
