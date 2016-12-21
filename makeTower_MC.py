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

height = 5
posdata = getposition()
try:
    #blocktype = int(input("어떤 블록으로 탑을 만들까요? (TNT46, 크리스탈95, 레드스톤블록152, 빛나는유리블록138)"))
    blocktype = 138

    for roopy in range(0, 40, 2):
        for roopx in range(height):
            #makeblock(posdata.x, posdata.y + roop, posdata.z, blocktype)
            makeblock(posdata.x + roopx, posdata.y, posdata.z + roopy, blocktype)
except:
    print("숫자만 입력하세요")
