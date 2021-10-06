import controller
import model   # Pass a reference to this module when calling each update in update_all

#Use the reference to this module to pass it to update methods

from ball      import Ball
from floater   import Floater
from blackhole import Black_Hole
from pulsator  import Pulsator
from hunter    import Hunter
from special   import Special


# Global variables: declare them global in functions that assign to them: e.g., ... = or +=

running     = False
cycle_count = 0
simultons_set = set()
selection = None

#return a 2-tuple of the width and height of the canvas (defined in the controller)
def world():
    return (controller.the_canvas.winfo_width(),controller.the_canvas.winfo_height())

#reset all module variables to represent an empty/stopped simulation
def reset ():
    global running, cycle_count, simultons_set
    running = False
    cycle_count = 0
    simultons_set = set()


#start running the simulation
def start ():
    global running
    running = True


#stop running the simulation (freezing it)
def stop ():
    global running
    running = False


#step just one update in the simulation
def step ():
    global cycle_count
    cycle_count += 1
    for item in simultons_set:
        item.update()


#remember the kind of object to add to the simulation when an (x,y) coordinate in the canvas
#  is clicked next (or remember to remove an object by such a click)   
def select_object(kind):
    global selection
    #change global var "selection" to the object that is remembered
    selection = kind



#add the kind of remembered object to the simulation (or remove all objects that contain the
#  clicked (x,y) coordinate
def mouse_click(x,y):
    if selection == None:
        pass
    elif selection == 'Remove':
        copy_set = set(simultons_set)
        for sim in copy_set:        
            if sim._x >= x - 5 and sim._x <= x + 5 and sim._y >= y - 5 and sim._y <= y + 5:
                remove(sim)
    else:
        simultons_set.add(eval('{}(x,y)'.format(selection)))


#add simulton s to the simulation
def add(s):
    simultons_set.add(s)
    

# remove simulton s from the simulation    
def remove(s):
    global simultons_set
    copy_set = set(simultons_set)
    copy_set.remove(s)
    simultons_set = copy_set

    

#find/return a set of simultons that each satisfy predicate p    
def find(p):
    res = set()
    for i in simultons_set:
        if p(i):
            res.add(i)
    return res


#call update for every simulton (passing each model) in the simulation
#this function should loop over one set containing all the simultons
#  and should not call type or isinstance: let each simulton do the
#  right thing for itself, without this function knowing what kinds of
#  simultons are in the simulation
def update_all():
    global cycle_count
    if running:
        cycle_count += 1
        for item in simultons_set:
            item.update()


#To animate: first delete every simulton from the canvas; then call display on
#  each simulton being simulated to add it back to the canvas, possibly in a
#  new location; also, update the progress label defined in the controller
#this function should loop over one set containing all the simultons
#  and should not call type or isinstance: let each simulton do the
#  right thing for itself, without this function knowing what kinds of
#  simultons are in the simulation
def display_all():
    for o in controller.the_canvas.find_all():
        controller.the_canvas.delete(o)
    
    for s in simultons_set:
        s.display(controller.the_canvas)
    
    controller.the_progress.config(text=str(len(simultons_set))+" simultons/"+str(cycle_count)+" cycles")
