# def equa(x,w,a,y=1,z=1):
#     x1=x*2
#     x2=y*3
#     x3=z*4
#     return x1+x2+x3
#
#
#
# y=equa(10,20,30) #positional args
# y1 = equa(z=30,y=20,x=10) #keyword arguments
# y2 = equa(y=10,z=20) #default arguments
# print('y:',y)
# print('y1:',y1)
# print('y2:',y2)

#
# def sum(name,*args):
#     sum=0
#     for i in args:
#         sum+=i
#     print('sum for {} is {}'.format(name,sum))
#
# sum('ashok',10,20,30,40)
# sum('john',10,33,40)

#key word arguments
# def display(name,**kwargs):
#     for x,y in kwargs.items():
#         print('name={},key={},value={}'.format(name,x,y))
#
# display('tom',id=100,sal=30000)
# display('tim',id=1001,loc='del',dept='fin')


#multi value returning
# def equation_xxxxxxxxx(x,y=1,z=1):
#     x1=x*2
#     x2=y*3
#     x3=z*4
#     return x1,x2,x3
#
# # y1,y2,y3=equa(12,13,14)
# # print(y1)
# # print(y2)
# # print(y3)
#
# f = equation_xxxxxxxxx
#
# y1,y2,y3=f(10,20,30)
# print(y1)
# print(y2)
# print(y3)


# a=0
# b=10
# def displ():
#     a=20 #local
#     b= 30 #local
#     # global b
#     print('local a:',a)
#     print('global a:',globals()['a'])
#     print('global b:',globals()['b'])

# def displ1():
#     print('a:',a)
#     print('b:',b)

# displ()
# displ1()
