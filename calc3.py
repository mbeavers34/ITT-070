
# Header------------------------------------------
# Functions --------------------------------------
class cal():                               #Create calculator class
    def __init__(self,a,b):
        self.a=a                           # properties of the object
        self.b=b                           # properties of the object
    def add(self):                         # Dont need properties they are inherited 
        return self.a+self.b
    def mul(self):
        return self.a*self.b
    def div(self):
        return self.a/self.b
    def sub(self):
        return self.a-self.b
#Main------------------------------------------------
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
equation=cal(a,b)                           # create the object
choice=1
while choice!=0:
    print("0. Exit")
    print("1. Add")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice=int(input("Enter choice: "))
    if choice==1:
        print("Result: ",equation.add())
    elif choice==2:
        print("Result: ",equation.sub())
    elif choice==3:
        print("Result: ",equation.mul())
    elif choice==4:
              print("Result: ",round(equation.div(),2))
    elif choice==0:
        print("Exiting!")
    else:
        print("Invalid choice!!")
 
 
print()
