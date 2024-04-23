# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 14:29:24 2024
@author: mbeavers
Programe name : Battle
Turn based game where charcter can loos or gain stamina based on actions
"""

class GameCharacter:
    def __init__(self, name, stamina, action):
        self.name = name
        self.stamina = stamina
        self.action = action

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
        
    def strike(self):
        print(f"{self.name} is striking.")
        self.stamina -= 10
        self.action = 'strike'
        print(f"{self.name}'s stamina decreased to {self.stamina}.")
        
    def help(self):
        print("         Stamina" )
        print("w = walk     -5\nr = rest    +20\nb = block   -10\ns = strike  -20\nq = quit" )
        print(f"{self.name}'s last action was {self.action}.")