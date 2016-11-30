import turtle as tt

def change_pos(xpos, ypos):
    tt.penup()
    tt.setpos(xpos, ypos)
    tt.pendown()

def draw_line(angle, size):
    tt.fd(size)
    tt.rt(360/angle)

angleNum = int(input("Which do you like draw figure? (3/4/5/6/8)"))
change_pos(angleNum * -10, angleNum * 10)
for loopCounter in range(angleNum):
    draw_line(angleNum, angleNum * 10)
