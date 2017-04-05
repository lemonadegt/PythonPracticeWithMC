import random
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
blockType = 138

'''
def makeStation

def makeStairs

def makeBridge
'''

pos = mc.player.getPos()
x = int(pos.x)
y = int(pos.y)
z = int(pos.z)

rx = random.randint(-10, 10)
ry = random.randint(5, 10)
rz = random.randint(-10, 10)

mc.setBlocks(x+rx-1, y+ry-1, z+rz-1, x+rx, y+ry, z+rz, blockType)

for i in range(ry+2):
    mc.setBlock(x+rx, y+ry-i, z+rz-i, blockType)
    mc.setBlock(x+rx+1, y+ry-i, z+rz-i, blockType)

