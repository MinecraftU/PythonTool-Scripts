# Imports
import mcpi.minecraft as minecraft
import mcpi.block as block
import random
import time

# Get the Minecraft World Handle
mc = minecraft.Minecraft.create()

# Block type 
blocktype = [block.AIR.id, block.STONE.id]

# Wall Height/Width Params
HEIGHT = 4
WIDTH = 9

pos = mc.player.getTilePos()

# Generate Platform
mc.setBlocks(pos.x - WIDTH//2, pos.y - 1, pos.z - WIDTH//2, pos.x + WIDTH//2, pos.y - 1, pos.z + WIDTH//2, block.IRON_BLOCK.id)
mc.setBlock(pos.x, pos.y - 1, pos.z, block.GOLD_BLOCK.id)

# Setup Position for Generating Walls Easier
pos.x -= WIDTH//2
pos.y += HEIGHT - 1
pos.z += (WIDTH//2 + 1)

# Loop for Moving Walls
while True:
	# Set Random Blocks for Wall
	wall = []
	for i in range(WIDTH*HEIGHT):
		wall.append(blocktype[random.randint(0,1)])
	
	# Reset Position for Generating New Wall
	pos.z -= (WIDTH + 1)
	time.sleep(1)
	
	# Loop to Make Walls Move
	for a in range(WIDTH + 1):
		# Generate Wall
		n = 0
		pos.z += 1
		pos.y -= HEIGHT
		for b in range(HEIGHT):
			pos.y += 1
			for c in range(WIDTH):
				mc.setBlock(pos.x + c, pos.y, pos.z, wall[n])
				n += 1
		
		# Remove Previous Wall
		n = 0
		pos.y -= HEIGHT
		time.sleep(0.5)
		for b in range(HEIGHT):
			pos.y += 1
			for c in range(WIDTH):
				mc.setBlock(pos.x + c, pos.y, pos.z, block.AIR.id)
				n += 1
