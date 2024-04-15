# Header------------------------------------------
#Name Michael Beavers
#Date 4/15/2024
#Program: calc3.py
#Description: Simple text base calculator
# Functions --------------------------------------
class calc():                               #Create calculator class
    def __init__(self,a,b):
        self.a=a                           # properties of the object
        self.b=b                           # properties of the object
  
    def add(self):                         # Dont need properties they are inherited 
        return self.a+self.b
  
    def sub(self):
        return self.a-self.b
  
    def mul(self):
        return self.a*self.b
  
    def div(self):
        return self.a/self.b
    
#Main------------------------------------------------
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
equation=calc(a,b)                           # create the object
choice=1
while choice!=0:
    print("0. Exit")
    print("1. Add")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice=int(input("Enter choice: "))
    if choice==1:
        print(f'\n {a}+{b}={equation.add()}\n')
    elif choice==2:
        print(f'\n {a}-{b}={equation.sub()}\n')
    elif choice==3:
        print(f'\n {a}+{b}={equation.mul()}\n')
    elif choice==4:
        print(f'\n {a}+{b}={round(equation.div(),3)}\n')
    elif choice==0:
        print("Exiting!")
    else:
        print("Not a valid choice. Please try again!!")
 
print()
