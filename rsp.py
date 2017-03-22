import random

GAWI = "가위"
BAWI = "바위"
BO = "보"
DRAW = "무승부"
WIN = "당신의 승리"
LOSE = "당신의 패배"
rockscissorspaper = [GAWI, BAWI, BO]
states = [DRAW, WIN, LOSE]
result = ''

selectednum = int(input("가위 바위 보 중에서 선택해 주세요\n(가위 = 0, 바위 = 1, 보 = 2) : "))

while (selectednum < 0) or (selectednum > 2):
    selectednum = int(input("다시 선택해 주세요\n(가위 = 0, 바위 = 1, 보 = 2) : "))

comselectednum = random.randint(0,2)

if (selectednum - comselectednum) == 0:
    result = states[0]
elif (selectednum - comselectednum) == 1 or (selectednum - comselectednum) == -2:
    result = states[1]
else:
    result = states[2]

print("당신의 선택은 " + rockscissorspaper[selectednum])
print("컴퓨터의 선택은 " + rockscissorspaper[comselectednum])
print("결과는 " + result)
