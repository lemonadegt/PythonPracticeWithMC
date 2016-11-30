from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getTilePos()

print("Player x Position =", pos.x)
print("Player y Position =", pos.y)
print("Player z Position =", pos.z)
