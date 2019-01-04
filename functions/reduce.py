#reduce(function,sequence)
# x+y
# 1,2,3,4,5
# x=1,y=2
# x=3, y=3
# x=6 , y=4
# x=10, y=5
# x=15
#
# x*y
# x=1 y=2
# x=2 y=3
# x=6 y=4
# x=24 y=5
# x=120

list = range(1,10)
sum = reduce(lambda x,y:x+y,list)
print(sum)

multi = reduce(lambda x,y:x*y,list)
print(multi)
