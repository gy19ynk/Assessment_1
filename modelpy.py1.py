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
#random.shuffle
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

## show environment        
#matplotlib.pyplot.imshow(environment)


# Create agents
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

#def run():
    #print("run")
    #animation=matplotlib.animation.FuncAnimation(fig,update,frames=gen_function,repeat=False)    
    #canvas.show()
    #print("done")

#root = tkinter.Tk()
#root.wm_title("Model")
#canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
#canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

#root = tkinter.Tk() 
#menu_bar = tkinter.Menu(root)
#root.config(menu=menu_bar)
#model_menu = tkinter.Menu(menu_bar)
#menu_bar.add_cascade(label="Model", menu=model_menu)
#model_menu.add_command(label="Run model", command=run)

#matplotlib.pyplot.show()


#animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, frames=num_of_iterations, repeat=False)
#animation=matplotlib.animation.FuncAnimation(fig,update,frames=gen_function,repeat=False)


		   
#def run():
    #animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    #canvas.show()

#c = tkinter.Canvas(root, width=200, height=200)
#c.pack()
#c.create_rectangle(0, 0, 200, 200, fill="blue")
#tkinter.mainloop()

#matplotlib.pyplot.show()


#print(list_of_agents[0])
#print(list_of_agents[1])
#print(list_of_agents[len(list_of_agents) - 1])



#print(list_of_agents[0])
#print(list_of_agents[1])
#print(list_of_agents[len(list_of_agents) - 1])





##
#for agent in list_of_agents:
#    matplotlib.pyplot.scatter(agent.x,agent.y, color="red")
    


#Distance
#def distance_between(agents_row_a, agents_row_b):
#    return (((agents_row_a.x - agents_row_b.x)**2) +
#    ((agents_row_a.y - agents_row_b.y)**2))**0.5
#answer = ( ( (y0 - y1) **2 ) + ( (x0 - x1) **2 ) ) ** 0.5
#print (answer) 
#
#matplotlib.pyplot.show()





# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
matplotlib.pyplot.ylim(0, 100)
"""

tkinter.mainloop()





     