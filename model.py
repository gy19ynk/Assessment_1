
#the model runs and  allows agents to interact with the environment
#
#runs until some number of steps reached or a stopping condition reached


#generates random variable
import random

import time 
import operator
#adds matplotlib builtins
import matplotlib
matplotlib.use('TkAgg')
#creates figures and axes to achieve the desired plot
import matplotlib.pyplot
#animates the 
import matplotlib.animation
#adds the agents created in the agentframework 
import agentframework
#reads the csv file
import csv
#adds tkinter and opens a window demonstrating a simple Tk interface
import tkinter


#runs model in line with the event based programming model
def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.draw()

#creates figure
fig = matplotlib.pyplot.figure(figsize=(7, 7))

#builds main window; sets title, creates and lays out a matplotlib canvas embedded within our window linked with matplotlib figure
root = tkinter.Tk() #main window
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

#simple event based programming model
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)


random.seed(1)
num_of_agents = 10
num_of_iterations = 100
   
neighbourhood = 20
list_of_agents = []

# Loads environment(code which represents the world that agents may interact with)
print("Load environment")
#reads the csv file of the 
environment = []
with open("in.txt", newline='') as f:
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    for line in reader:
        rowlist=[]
        for value in line:
            rowlist.append(value)
        environment.append(rowlist)




# Creates agents
print("Create agents")
for i in range(num_of_agents):
    list_of_agents.append(agentframework.Agents(i, list_of_agents,environment))
    
carry_on = True	

	
def update(frame_number):
    print("frame_number", frame_number)
    global carry_on
    
    fig.clear()   
    
#    global environment
#    global list_of_agents
# Move and eat
    for j in range(num_of_iterations):
        for i in range(num_of_agents):
            list_of_agents[i].move()
            list_of_agents[i].eat()
            list_of_agents[i].share_with_neighbours(neighbourhood)
            

    matplotlib.pyplot.xlim(0,300)  
    matplotlib.pyplot.ylim(0,300) 
    matplotlib.pyplot.imshow(environment)
    
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(list_of_agents[i].x,list_of_agents[i].y)


    # show environment    
    matplotlib.pyplot.draw()
		
def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
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





     