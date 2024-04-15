# Header---------------------------------------------------
# Functions------------------------------------------------
class Dog:                                        # Create class
     species = "Canis familiaris"                 # Inherited   
     def __init__(self, name, age, sound):
         self.name = name                         # Attribute
         self.age = age                           # Attribute   
         self.sound = sound                       # Attribute     
     def bark(self):                              # Method
         print(self.sound)
# Variables-----------------------------------------------

# Main---------------------------------------------------
#miles = Dog("Miles", 4, "woof")                   # objects
buddy = Dog("Buddy", 9, "")                       # objects
#buddy.sound ="yip yip"

print(buddy.age)
#print(miles.species)
#buddy.bark()
#miles.bark()
