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
    x = targetpos.x
    y = targetpos.y
    z = targetpos.z
    blocktype = 41
    mc.setBlocks(x, y, z, x + random.randint(50, 100), y + random.randint(50, 100), z + random.randint(50, 100), blocktype)

pos = getposition()
makeblock(pos)
setposition(pos)

starttime = time.clock()

# 금블록을 찾을 때까지
while mc.getBlock(mc.player.getTilePos()) == 41:
    endtime = time.clock()
    timeGap = endtime - starttime

    gapChatMessage = "금블록을 찾을 때까지 " + str(int(timeGap)) + "초가 걸렸어요!"
    mc.postToChat(gapChatMessage)
