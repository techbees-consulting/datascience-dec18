class Human:
    gender ="male" #class variable
    def __init__(self,name,age,loc):
        self.name=name
        self.age=age
        self.loc=loc
        print('print in constructor')
    # method
    def display(self):
        '''my first method'''
        print('name: ',self.name)
        print('age: ',self.age)
        print('loc: ',self.loc)

    @classmethod
    def display(cls):
        print('hello')

    @staticmethod
    def display():
        print('hellow')


ram = Human('Ram',35,'del')
print(ram.name)

tom = Human('Tom',25,'mum')
print(tom.name)
print(ram.gender)
print(Human.gender)
