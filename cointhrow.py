import random

maxthrowcount = 30000
currthrowcount = 0
coin_front = 0
coin_back = 0

for i in range(maxthrowcount):
    coinstatus = random.randint(0,1)
    currthrowcount += 1

    if coinstatus == 0:
        coin_front += 1
    else:
        coin_back += 1

print("동전을 던진 횟수는", str(currthrowcount), "입니다.")
print("앞면은 %d번 나왔으며 확률은 %1.3f%% 입니다" %(coin_front, coin_front/currthrowcount))
print("뒷면은 %d번 나왔으며 확률은 %1.3f%% 입니다" %(coin_back, coin_back/currthrowcount))
