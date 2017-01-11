import getpass
import random

GAWI = "가위"
BAWI = "바위"
BO = "보"
rockscissorspaper = [GAWI, BAWI, BO]

selectednum = int(input("가위 바위 보 중에서 선택해 주세요\n(가위 = 0, 바위 = 1, 보 = 2) : "))
#selectednum = int(getpass.getpass("가위 바위 보 중에서 선택해 주세요\n(가위 = 0, 바위 = 1, 보 = 2) : "))

while (selectednum < 0) or (selectednum > 2):
    selectednum = int(input("다시 선택해 주세요\n(가위 = 0, 바위 = 1, 보 = 2) : "))
    #selectednum = int(getpass.getpass("다시 선택해 주세요\n(가위 = 0, 바위 = 1, 보 = 2) : "))

comselectednum = random.randint(0,2)

print("당신의 선택은 " + rockscissorspaper[selectednum])
print("컴퓨터의 선택은 " + rockscissorspaper[comselectednum])


#16번 과제
#컴퓨터가 항상 이기기
#사용자의 선택 가리기


'''
print(rockscissorspaper)
print(rockscissorspaper[0])
print(rockscissorspaper[1])
print(rockscissorspaper[2])

print(len(rockscissorspaper))

for loopi in range(0, len(rockscissorspaper)):
    print(rockscissorspaper[loopi])

for loopi in rockscissorspaper:
    print(loopi)
'''
