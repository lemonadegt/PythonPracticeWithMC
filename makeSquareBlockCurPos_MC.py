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
    blocktype = 46 #용암10,TNT46, 레드스톤블록152
    mc.setBlock(x, y, z, blocktype)

pos = getposition()
oldzpos = pos.z

for counterNumX in range(10):
    pos.x += 1
    pos.z = oldzpos
    for counterNumY in range(10):
        pos.z += 1
        makeblock(pos)
