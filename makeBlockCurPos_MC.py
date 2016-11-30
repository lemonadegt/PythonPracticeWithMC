from mcpi.minecraft import Minecraft
mc = Minecraft.create()

def getposition():
    curpos = mc.player.getTilePos()
    return curpos

def setposition(destpos):
    mc.player.setTilePos(destpos)

def makeblock(targetpos):
    x = targetpos.x
    y = targetpos.y
    z = targetpos.z
    blocktype = 10
    mc.setBlock(x, y, z, blocktype)

for counterNumber in range(30):
    pos = getposition()
    pos.y += 1
    makeblock(pos)
    setposition(pos)
