from mcpi.minecraft import Minecraft
mc = Minecraft.create()

answer = input("Create a crater? Y / N")

while (answer.upper() != "Y") and (answer.upper() != "N"):
    answer = input("Create a crater? Just Y / N")

if answer.upper() == "Y":
    pos = mc.player.getPos()
    mc.setBlocks(pos.x + 1, pos.y + 1, pos.z + 1, pos.x - 1, pos.y - 1, pos.z - 1, 0)
    mc.postToChat("Boom!")
