import turtle as tt

def change_pos(xpos, ypos):
    tt.penup()
    tt.setpos(xpos, ypos)
    tt.pendown()

def draw_line(angle, size):
    tt.fd(size)
    #tt.rt((360/angle))
    tt.rt(144)

tt.color('red')

# Pentagon
angleNum = 5
change_pos(-100, 100)
tt.begin_fill()
for loopCounter in range(angleNum):
    draw_line(angleNum, angleNum * 50)
tt.end_fill()

input()