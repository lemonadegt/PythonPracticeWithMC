import time
import math
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos1 = mc.player.getTilePos()
x1 = pos1.x
y1 = pos1.y
z1 = pos1.z
time1 = time.clock()

while mc.getBlock(mc.player.getTilePos()) != 9:
    mc.postToChat("The player moving!")

pos2 = mc.player.getTilePos()
x2 = pos2.x
y2 = pos2.y
z2 = pos2.z
time2 = time.clock()

xDistance = x2 - x1
yDistance = y2 - y1
zDistance = z2 - z1

distance = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
timeGap = time2 - time1

positionChatMessage = "The player has moved x:" + str(xDistance) + " y:" + str(yDistance) + " z:" + str(zDistance)
mc.postToChat(positionChatMessage)

distanceChatMessage = "The player has moved " + str(int(distance)) + " blocks"
mc.postToChat(distanceChatMessage)

gapChatMessage = "The player spend " + str(int(timeGap)) + "(s) moving time"
mc.postToChat(gapChatMessage)
