import turtle as tt

def change_pos(xpos, ypos):
    tt.penup()
    tt.setpos(xpos, ypos)
    tt.pendown()

def draw_line(angle, size):
    tt.fd(size)
    tt.rt(360/angle)

# Triangle
change_pos(-100, 100)
draw_line(3, 30)
draw_line(3, 30)
draw_line(3, 30)

# Square
change_pos(0, 100)
draw_line(4, 40)
draw_line(4, 40)
draw_line(4, 40)
draw_line(4, 40)

# Pentagon
change_pos(100, 100)
draw_line(5, 50)
draw_line(5, 50)
draw_line(5, 50)
draw_line(5, 50)
draw_line(5, 50)

# Hexagon
change_pos(-100, -50)
draw_line(6, 60)
draw_line(6, 60)
draw_line(6, 60)
draw_line(6, 60)
draw_line(6, 60)
draw_line(6, 60)

# Octagon
change_pos(100, -50)
draw_line(8, 80)
draw_line(8, 80)
draw_line(8, 80)
draw_line(8, 80)
draw_line(8, 80)
draw_line(8, 80)
draw_line(8, 80)
draw_line(8, 80)
