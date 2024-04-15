'''
    A simple calculator using oop in python
'''



# A calculator class
class Calculate:
    def __init__(self, a, b):
        self.x = a
        self.y = b
    
    # functions to define our operators (+,-,*,/)
    @staticmethod
    def add(self):
        return (self.x+self.y)   
    
    @staticmethod
    def sub(self):
        return self.x-self.y

    @staticmethod
    def mul(self):
       return x * y
       
    @staticmethod
    def div(self):
        return x / y

    # Define a function to get our integer inputs   
    @staticmethod
    def get_numbers():
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        return num1, num2



#Main_______________________________________________________
num1,num2 = Calculate.get_numbers()
equation1 = Calculate(num1,num2)
print(Calculate.add(equation1))
