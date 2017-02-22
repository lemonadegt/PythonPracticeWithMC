from mcpi.minecraft import Minecraft
mc = Minecraft.create()

def cleantheroad():
    pos = mc.player.getPos()
    mc.setBlocks(pos.x + 1, pos.y + 3, pos.z + 1, pos.x - 1, pos.y, pos.z - 1, 0)
    mc.postToChat("길을 비켜라!")

while True:
    cleantheroad()
