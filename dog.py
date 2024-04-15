class Dog:
     species = "Canis familiaris"
     def __init__(self, name, age, sound):
         self.name = name
         self.age = age
         self.sound = sound   
     def bark(self):
         print(self.sound)
         
miles = Dog("Miles", 4, "woof")
buddy = Dog("Buddy", 9, "")
buddy.sound ="yip yip"


print(buddy.age)
print(miles.species)
buddy.bark()
miles.bark()
