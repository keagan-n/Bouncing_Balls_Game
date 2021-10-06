# Black_Hole inherits from only Simulton, updating by finding+removing
#   any Prey whose center is contained within its radius
#  (returning a set of all eaten simultons), and
#   displays as a black circle with a radius of 10
#   (width/height 20).
# Calling get_dimension for the width/height (for
#   containment and displaying) will facilitate
#   inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey

import model

class Black_Hole(Simulton):
    
    radius = 10
    
    def __init__(self,x,y):
        Simulton.__init__(self, x, y, 20, 20)
    
    def update(self):
        sim_eaten = model.find(lambda obj: self.contains(obj))
        for sims in sim_eaten:
            if sims in model.simultons_set:
                model.remove(sims)
        return sim_eaten
    
    def display(self,canvas):
        width, height = self.get_dimension()
        canvas.create_oval(self._x-width, self._y-height,self._x+width, self._y+height,fill = "black")
        #canvas.create_oval(self._x-Black_Hole.radius, self._y-Black_Hole.radius,self._x+Black_Hole.radius, self._y+Black_Hole.radius,fill = "black")
    
    def contains(self, xy):
        distance_from = self.distance((xy._x,xy._y))
        if isinstance(xy, Prey) and distance_from < self._width:
            return True