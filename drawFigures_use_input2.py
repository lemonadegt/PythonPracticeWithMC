import turtle as tt

def change_pos(xpos, ypos):
    tt.penup()
    tt.setpos(xpos, ypos)
    tt.pendown()

def draw_line(angle, size):
    angle = angle + 3
    tt.fd(size)
    tt.rt(360/angle)

angleNum = int(input("어떤 다각형을 그릴까요? (3/4/5/6/8)"))
change_pos(angleNum * -10, angleNum * 10)
for loopCounter in range(angleNum):
    draw_line(angleNum, 100)
print("메인의 angleNum: ", angleNum)

