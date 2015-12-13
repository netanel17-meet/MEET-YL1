from turtle import *
from meet import *
import random
cells=[]

colors=["green","blue","red","pink","yellow","orange"]
for x in range(0,20):
    cell ={"x":random.randint(-50,50), "y":random.randint(-50,50), "dx":random.randint(1,5), "dy":random.randint(1,5), "radius":random.randint(5,100), "color":random.choice(colors)}
    cell=create_cell(cell)
    cells.append(cell)

def borders(cells):
    for cell in cells:
        w= meet.get_screen_width()
        h= meet.get_screen_height()
        x= cell.xcor()
        y= cell.ycor()
        r = cell.get_radius()
        if (x+r>w):
           cell.set.dx(-cell_get_dx())
        elif (x+r<-w):
           cell.set.dx(-cell_get_dx())
        elif(y+r>h):
           cell.set.dy(-cell_get_dy())
        elif (y+r<-h):
           cell.set.dy(-cell_get_dy())









while True:
	move_cells(cells)

mainloop()

