"""
Created on Tue Apr 23 14:29:24 2024
@author: mbeavers
Programe name : Battle
Turn based game where charcter can loos or gain stamina based on actions
"""

class GameCharacter:
    def __init__(self, name, stamina, action, health):
        self.name = name
        self.stamina = stamina
        self.action = action
        self.health = health

    def walk(self):
        print(f"{self.name} is walking.")
        self.stamina = max (self.stamina -5, 0)
        self.action = 'walk'
        print(f"{self.name}'s stamina decreased to {self.stamina}.")

    def rest(self):
        print(f"{self.name} is resting.")
        self.stamina += 20
        self.action = 'rest'
        print(f"{self.name}'s stamina increased to {self.stamina}.")
    
    def block(self):
        print(f"{self.name} is blocking.")
        self.stamina -= 10
        self.action = 'block'
        print(f"{self.name}'s stamina decreased to {self.stamina}.")
        
    def strike(self, target):
        print(f"{self.name} is striking {target.name}.")
        self.stamina -= 10
        self.action = 'strike'
        target.health -= 20
        print(f"{self.name}'s stamina decreased to {self.stamina}.")
        print(f"{target.name}'s health decreased to {target.health}.")
        
    def help(self):
        print("         Stamina" )
        print("w = walk     -5\nr = rest    +20\nb = block   -10\ns = strike  -20\nq = quit" )
        print(f"{self.name}'s last action was {self.action}.")
#Variables
turn="" 
name = ""
target = ""

#Characters---------------------------------------------------------------
hero = GameCharacter("Hero", 100,"Rest", 100)
blade = GameCharacter("Blade", 100,"Rest", 100) 
#Main---------------------------------------------------------------------
while turn != "q":
    turn = input("----------------------------\nHero - w,r,b,s,q h=help: ").lower()
    if input == "w":
        hero.walk()
    elif turn=="r":
        hero.rest()
    elif turn=="b":
        hero.block()
    elif turn == "s":
        target = input("Who did you want to strike? ").lower()
        if target == 'blade':
            target = blade
            hero.strike(target)
        else:
            print(f"{hero.name} swings his weapon wildly at an imaginary person called {target}")
    elif turn == "h":
        hero.help() 
        

    turn = input("----------------------------\nBlade -w,r,b,s,q h=help: ").lower()
    if input == "w":
        blade.walk()
    elif turn=="r":
        hero.rest()
    elif turn=="b":
        blade.block()
    elif turn == "s":
        target = input("Who did you want to strike? ").lower()
        if target == 'hero':
            target = hero
            blade.strike(target)
        else:
            print(f"{blade.name} swings his weapon wildly at an imaginary person called {target}")
    elif turn == "h":
        blade.help()