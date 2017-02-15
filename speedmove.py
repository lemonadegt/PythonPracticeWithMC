from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()

def getposition():
    curpos = mc.player.getTilePos()
    return curpos

def setposition(destpos):
    x = destpos.x + 30
    y = destpos.y
    z = destpos.z + 30
    mc.player.setTilePos(x, y, z)

while True:
    pos = getposition()
    x = pos.x
    y = pos.y
    z = pos.z
    mc.postToChat(" CurPos: %d, %d, %d" % (x, y, z))

    time.sleep(3)

    pos = getposition()
    setposition(pos)
    mc.postToChat(" CurPos: %d, %d, %d" % (x, y, z))