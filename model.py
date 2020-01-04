
#The model is run using the agents and environment that are called and intitialised in the agentframework.
#The model allows agents to interact with the environment until some number of steps reached or a stopping condition reached
#The environment is in the form of raster data with values that represent a pixel of the image arranged in a grid

#generates random variable
import random
#adds matplotlib builtins and Agg rendering to a Tk canvas
import matplotlib
matplotlib.use('TkAgg')
#creates figures and axes  to achieve the desired plot
import matplotlib.pyplot
#animates the model
import matplotlib.animation
#adds the agents created in the agentframework 
import agentframework
#reads the csv file
import csv
#adds tkinter and opens a window demonstrating a simple Tk interface
import tkinter


#Makes an animation by repeatedly calling functions.
def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.draw()

#creates new figures that the environment  
fig = matplotlib.pyplot.figure(figsize=(7, 7))

#builds main window, sets title, creates and lays out a matplotlib canvas embedded within our window linked with figure
root = tkinter.Tk() #main window
root.wm_title("Model") #window and title to run model
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

#initialises random number generator
random.seed(1)
#total number of agents and the repetitions each agent runs
num_of_agents = 10
num_of_iterations = 100
#creates a list of agents that are close to each other and  share resources  
neighbourhood = 20
list_of_agents = []

# Loads environment(code which represents the world that agents may interact with)
print("Load environment")
#makes an empty list called environment
environment = []
#reads the csv file "in.txt" into the environment list
with open("in.txt", newline='') as f:
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    for line in reader:
        #makes an empty rowlist and adds values to the rowlist in the environment
        rowlist=[]
        for value in line:
            rowlist.append(value)
        environment.append(rowlist)




# Creates agents and adds list of agents to agents from the agentframework
print("Create agents")
for i in range(num_of_agents):
    list_of_agents.append(agentframework.Agents(i, list_of_agents,environment))
    
carry_on = True	

#Gets the index of the agents to update in frame	
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
            

    matplotlib.pyplot.xlim(0,300)  #plots x values 
    matplotlib.pyplot.ylim(0,300) #plots y values
    matplotlib.pyplot.imshow(environment) #plots and shows environment
    
    for i in range(num_of_agents):
        #creates scatter plot of the list of agents
        matplotlib.pyplot.scatter(list_of_agents[i].x,list_of_agents[i].y) 
     # updates the pyplot or  environment plot  
    matplotlib.pyplot.draw() 
    
    
#returns the function so that it is resumable		
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





     
