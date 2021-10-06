# Hunter inherits from the Pulsator (1st) and Mobile_Simulton (2nd) classes:
#   updating/displaying like its Pulsator base, but also moving (either in
#   a straight line or in pursuit of Prey), like its Mobile_Simultion base.


from prey import Prey
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from math import atan2

import model
class Hunter(Pulsator, Mobile_Simulton):
    
    dist_constant = 200
    
    def __init__(self,x,y): 
        Pulsator.__init__(self, x, y)
        Mobile_Simulton.__init__(self, x, y, 20, 20, 0,5)
        self.randomize_angle()
        
    def update(self):
        eaten = Pulsator.update(self)
        self_coords = self.get_location()
        
        def helper(obj):
            check = False
            if isinstance(obj, Prey) and self.distance(obj.get_location()) <= Hunter.dist_constant:
                check = True
            return check
        
        close_objects = model.find(lambda x: helper(x))
        if close_objects:
            closest = min([(self.distance(sim.get_location()),sim )for sim in close_objects])
            close_obj = closest[1]
            
            obj_coords = close_obj.get_location()
            self.set_angle(atan2(obj_coords[1]-self_coords[1],obj_coords[0]-self_coords[0]))
            
        self.move()
        return eaten