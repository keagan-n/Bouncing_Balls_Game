# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage


#from PIL.ImageTk import PhotoImage
from prey import Prey
import random as rand


class Floater(Prey): 
    
    radius = 5
    
    def __init__(self, x, y):
        Prey.__init__(self, x, y, 10, 10, 0, 5)
        self.randomize_angle()
    
    def update(self):
        self.move()
        percent_time = rand.randint(1,100)
        if percent_time <= 30:
            change_val = rand.uniform(-0.5,0.5)
            if self._speed + change_val >= 3 and self._speed + change_val <= 7:
                self._speed += change_val
            self._angle += rand.uniform(-0.5,0.5)

        self.wall_bounce()
    
    def display(self,canvas):
        canvas.create_oval(self._x-Floater.radius, self._y-Floater.radius,self._x+Floater.radius, self._y+Floater.radius,fill = "red")

