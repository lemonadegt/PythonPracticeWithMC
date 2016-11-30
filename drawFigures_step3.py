import turtle as tt

def change_pos(xpos, ypos):
    tt.penup()
    tt.setpos(xpos, ypos)
    tt.pendown()

def draw_line(angle, size):
    tt.fd(size)
    tt.rt(360/angle)

# for counter in range(start, stop, step)
# for counter in range(start, stop)
# for counter in range(stop)

# Triangle
angleNum = 3
change_pos(-100, 100)
for loopCounter in range(angleNum):
    draw_line(angleNum, angleNum * 10)

# Square
angleNum = 4
change_pos(0, 100)
for loopCounter in range(angleNum):
    draw_line(angleNum, angleNum * 10)

# Pentagon
angleNum = 5
change_pos(100, 100)
for loopCounter in range(angleNum):
    draw_line(angleNum, angleNum * 10)

# Hexagon
angleNum = 6
change_pos(-100, -50)
for loopCounter in range(angleNum):
    draw_line(angleNum, angleNum * 10)

# Octagon
angleNum = 8
change_pos(100, -50)
for loopCounter in range(angleNum):
    draw_line(angleNum, angleNum * 10)
