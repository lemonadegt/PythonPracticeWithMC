from mcpi.minecraft import Minecraft

mc = Minecraft.create()

def getposition():
    curpos = mc.player.getTilePos()
    return curpos

def setposition(destpos):
    mc.player.setTilePos(destpos)

def makeblock(x, y, z):
    blockType = 138  # 용암10,TNT46, 레드스톤블록152
    size = 10
    mc.setBlocks(x, y, z, x + size, y + size, z + size, blockType)
    #mc.setBlock(x, y, z, blocktype)

pos = getposition()
makeblock(pos.x, pos.y, pos.z)

#for counterNumH in range(10):
#    for counterNumX in range(10):
#        for counterNumY in range(10):
#            makeblock(pos.x + counterNumX, pos.y + counterNumH, pos.z + counterNumY)


