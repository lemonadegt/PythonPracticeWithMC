import random

mina = random.randint(2, 9)
bora = random.randint(1, 9)

sejeong = int(input("%d x %d 는 몇일까? : " %(mina, bora)))

if sejeong == (mina * bora):
    print("오케이. %d 맞아요." %(mina * bora))
else:
    print("어휴. %d 인데 그것도 몰라?" %(mina * bora))
