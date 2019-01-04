class A:
    @staticmethod
    def add(a,b):
        return a+b

    @staticmethod
    def add(a,b,c):
        return a+b+c

    @staticmethod
    def display(msg):
        print('hey',msg)

    #
    def display(self):
        print('hey')

a = A()
A.display('good morning')
