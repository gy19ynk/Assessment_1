# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 16:24:56 2019

@author: 44781

"""

#The following code will call and build agents class by initialising them in a random location,and moves them in the environment before running the model.
import random
#creates a blue print of many agents
class Agents:
    
    #initialises the agents and their environment
    def __init__(self, i, agents, environment): 
        self.i = i
        self.x = random.randint(0,300) #initialise random integer x
        self.y = random.randint(0,300) #initialise random integer y
        self.agents = agents
        self.environment=environment
        self.store = 0
        
     #returns ID of the individual agents   
    def __str__(self): 
        return "ID=" + str(self.i) + ", store=" + str(self.store) + ", x=" + str(self.x) + ", y=" + str(self.y)
    
    #moves the individual agents
    def move(self): 
        
        if random.random() < 0.5:
            self.x= (self.x+1)% 300
        else :
            self.x=(self.x-1)%300
        
        if random.random() < 0.5:
             self.y= (self.y+1) % 300
        else :
            self.y=(self.y-1) %300 
            
    def eat(self):
         food = self.environment[self.x][self.y]
         if (food > 10):
             self.store = self.store + 10
             self.environment[self.y][self.x] = self.environment[self.y][self.x] - 10
         else:
             self.store = self.store + food
             self.environment[self.y][self.x] = self.environment[self.y][self.x] - food
    
    def distance_between(self, agent):
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5           
                
    def share_with_neighbours(self, neighbourhood):
         # Find neighbours
         for agent in self.agents:
             dist = self.distance_between(agent)
             if (dist < neighbourhood):
#                 print(self, "sharing with", agent, "distance", dist)
                 # Share with neighbours
                 total = self.store + agent.store
                 ave = total / 2
                 self.store = ave
                 agent.store = ave
                 # good sharing method
         pass 

 
       
        
                
            
           
        
            




