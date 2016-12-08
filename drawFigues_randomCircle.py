import turtle as tt
import random

def change_pos(xpos, ypos):
    tt.penup()
    tt.setpos(xpos, ypos)
    tt.pendown()

tt.speed(0)
radius = random.randint(10, 100)
for i in range(20):
    x = random.randint(-150, 150)
    y = random.randint(-150, 150)
    change_pos(x, y)
    tt.circle(radius)
