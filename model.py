import random
import time 
import operator
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot
import matplotlib.animation 
import agentframework
import csv
import tkinter



#
def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.draw()

#create figure
fig = matplotlib.pyplot.figure(figsize=(7, 7))

root = tkinter.Tk()
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

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

# Loads environment
print("Load environment")
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
            
#    if random.random() < 0.1:
#        carry_on = False
#        print("stopping condition")
    matplotlib.pyplot.xlim(0,300)  
    matplotlib.pyplot.ylim(0,300) 
    matplotlib.pyplot.imshow(environment)
    
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(list_of_agents[i].x,list_of_agents[i].y)
#        print(list_of_agents[i].x,list_of_agents[i].y)
#    print('finished')
    # show environment    
    #matplotlib.pyplot.show()
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

tkinter.mainloop()





     