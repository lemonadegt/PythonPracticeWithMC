import time
import random
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

def getposition():
    curpos = mc.player.getTilePos()
    return curpos

def setposition(destpos):
    x = destpos.x
    y = destpos.y + 50
    z = destpos.z
    mc.player.setTilePos(x, y, z)

def makeblock(targetpos):
    goldx = targetpos.x + random.randint(-10, 10)
    goldz = targetpos.z + random.randint(-10, 10)
    goldy = mc.getHeight(goldx, goldz)
    blocktype = 41
    mc.setBlock(goldx, goldy, goldz, blocktype)

    returnpos = targetpos
    returnpos.x = goldx
    returnpos.y = goldy
    returnpos.z = goldz
    return (returnpos)

pos = getposition()
gpos = makeblock(pos)
while True:
    x = pos.x
    y = pos.y
    z = pos.z
    mc.postToChat("GOLD: %d, %d, %d" % (gpos.x, gpos.y, gpos.z))
    mc.postToChat(" NOW: %d, %d, %d" % (x, y, z))
    if (int(gpos.x) == int(x)) and (int(gpos.z) == int(z)):
        mc.postToChat("*" * 50)
        break

#과제 20
#18업그레이드
#금블록까지 남은 거리를 x, y, z를 대화창에 출력
#어느쪽으로 가야 할지 방향을 대화창에 출력
#문자열 포맷 기능 적용
