from mcpi.minecraft import Minecraft

mc = Minecraft.create()

def getposition():
    curpos = mc.player.getTilePos()
    return curpos

def setposition(destpos):
    mc.player.setTilePos(destpos)

def makeblock(x, y, z):
    # 용암10,TNT46, 레드스톤블록152
    blockType = 138
    waterBlock = 8

    width = 6
    height = 4
    length = 4

    mc.setBlocks(x, y, z, x + width, y + height, z + length, blockType)
    mc.setBlocks(x + 1, y + 1, z + 1, x + width - 1, y + height, z + length - 1, waterBlock)

pos = getposition()
makeblock(pos.x, pos.y, pos.z)
