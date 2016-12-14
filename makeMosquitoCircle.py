import turtle as tt

def change_pos(xpos, ypos):
    tt.penup()
    tt.setpos(xpos, ypos)
    tt.pendown()

tt.speed(10)

for length in range(10, 300, 10):
    tt.circle(length, 180)

#for i in range(100):
#   tt.circle(i, extent=10)
