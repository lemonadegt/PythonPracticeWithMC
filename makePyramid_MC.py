from mcpi.minecraft import Minecraft

mc = Minecraft.create()

def getposition():
    curpos = mc.player.getTilePos()
    return curpos

def setposition(destpos):
    mc.player.setTilePos(destpos)

def makeblock(x, y, z, bt):
    blockType = 138  # 용암10,TNT46, 레드스톤블록152
    mc.setBlock(x, y, z, bt)

posdata = getposition()
x = posdata.x
y = posdata.y
z = posdata.z

try:
    blocktype = 138

    height = 5
    size = 1

    '''
    #Pyramid
    for roopy in range(size):
        for roopz in range(size):
           for roopx in range(size):
                makeblock(x + roopx, y, z + roopz, blocktype)

        size = size - 2
        x = x + 1
        y = y + 1
        z = z + 1
    '''

    '''
    #Use SetBlocks
    for i in range(size // 2 + 1):
        mc.setBlocks(x + i, y + i, z + i, x + size - i, y + i, z + size - i, blocktype)
    '''

    #Reverse Pyramid
    for roopy in range(height):
        for roopz in range(size):
           for roopx in range(size):
                makeblock(x - roopx, y, z - roopz, blocktype)

        size = size + 2
        x = x + 1
        y = y + 1
        z = z + 1

except:
    print("ERROR")
