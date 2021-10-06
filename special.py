# Special inherits from the Prey class and
#    it creates a mobile simulton object that 
#    is a green rectangle
# This Special object moves in a straight line but speeds up as it touches other Prey objects 
#    and periodically freezes if the speed is too fast (at speed 12)
# The simulton stays frozen until touched by a Prey object again
# Note: the same object cannot speed up the Special object consecutive times

import model
from prey import Prey

class Special(Prey):
    
    measure = 8
    
    def __init__(self,x,y):
        Prey.__init__(self, x, y, 16,16, 0, 3)
        self.randomize_angle()
        self.prev_touched = None


    def update(self):
        if self.get_speed() == 0:
            self.set_speed(0)
        else:
            self.move()
        touching = model.find(lambda x: self.touching(x))

        if len(touching) > 1 and touching != self.prev_touched:
            self.set_speed(self.get_speed()+1)
            if self.get_speed() == 12:
                self.set_speed(0)
            self.prev_touched = touching
 
        self.wall_bounce()
        
    def touching(self,obj):
        distance_from = self.distance((obj._x,obj._y))
        if isinstance(obj, Prey) and distance_from <= self._width:
            return True
    
    def display(self,canvas):
        canvas.create_rectangle(self._x-Special.measure, self._y-Special.measure,self._x+Special.measure, self._y+Special.measure,fill = "green")