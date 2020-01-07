#Agent Based Model created by Naomi Yankho Kalebe

#Run in Spyder

"""
The model is run using the agents and environment that are called and intitialised in the agentframework.Graphical User Interface used
(GUI)to run model.A window pops up when model is run. Use the option "Run model" on the menu bar to create agents in an 
environment. The Agents move, eat and share resources in the environment and sharing resources with each other under conditions
"""


"""
import operator exports a set of functions used in the model
"""

import random
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot
import matplotlib.animation
import agentframework
import csv
import tkinter


"""
Firsty, Initiate the variables
"""
random.seed(1)
num_of_agents = 10
num_of_iterations = 100 
neighbourhood = 20
list_of_agents = []
environment = []


"""
Thirdly, read the csv file 'in.txt' that is found in the repository  and create a 2D list
"""

print("Load environment")
with open("in.txt") as f:
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    for line in reader:
        rowlist=[]
        for value in line:
            rowlist.append(value)
        environment.append(rowlist)
fig = matplotlib.pyplot.figure(figsize=(7, 7))
       
"""
Then, initiate the agents
The agents are defined based on predefined X and Y list from the 'in.txt' folder of the environment
""" 
      




"""
Then update the frame and enable the agents to animate , thus move the agents and make them interact with each other 
and the environment
"""
def update(frame_number):
    print("frame_number", frame_number)
    global carry_on
    
    fig.clear()   
    matplotlib.pyplot.xlim(0,300)  #plots x values 
    matplotlib.pyplot.ylim(0,300) #plots y values
    matplotlib.pyplot.imshow(environment) #plots and shows environment

for j in range(num_of_iterations):
        for i in range(num_of_agents):
            list_of_agents[i].move()
            list_of_agents[i].eat()
            list_of_agents[i].share_with_neighbours(neighbourhood)
        for i in range(num_of_agents):
            matplotlib.pyplot.scatter(list_of_agents[i].x,list_of_agents[i].y)     
        matplotlib.pyplot.draw() 
        
print("Create agents")
for i in range(num_of_agents):
    list_of_agents.append(agentframework.Agents(i, list_of_agents,environment))
    
carry_on = True	
           

"""
Then, Display the plot of the environment and agents.
"""
def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.draw()


"""
Finally,initiate GUI and it's properties
""" 

#builds main window, sets title, creates and lays out a matplotlib canvas embedded within our window linked with figure
root = tkinter.Tk() 
root.wm_title("Model") 
#creates drawing area or playground for the figure
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
#packs the canvas and navigation toolbar into Tkinter's main window
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

#Adds a menu bar in Tkinter (main window)
menu_bar = tkinter.Menu(root)
#adds the file "model" in Tkinter
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
#adds command for initialising the running of model 
model_menu.add_command(label="Run model", command=run)






#Enable agents to animate until a stopping condition is reached, 100 iteration
def gen_function(b = [0]):
    a = 0
    global carry_on 
    while (a < num_of_iterations) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1






# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
matplotlib.pyplot.ylim(0, 100)
"""
#sets the GUI waiting for events and added at the very bottom of the file
tkinter.mainloop()





     
