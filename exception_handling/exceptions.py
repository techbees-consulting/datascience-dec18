# try:
#     li =[1,2,3]
#     print(li[5])
# except IndexError:
#     li.append(10)
#     print('invalid list element reference')
#
# else:
#     li.pop()
#     print('you are good to go')
#
# finally:
#     print('done')


try:
    a=int(input('enter a'))
    b=int(input('enter b'))
    print(a/b)
except ZeroDivisionError:
    print('Infinity')
    # print('denomiator should not be a zero')

