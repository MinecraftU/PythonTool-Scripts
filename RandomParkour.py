# Imports
import mcpi.minecraft as minecraft
import mcpi.block as block
import random
import time

# Get the Minecraft World Handle
mc = minecraft.Minecraft.create()

# Variables
pos = mc.player.getTilePos()
OPOS = pos
# Difficulty of the Game. 0 is Easiest, 8 is Hardest.
difficulty = 8

# Define Special Minecraft Parkour Jumps According to Difficulty
def skeppy(dis):
	if difficulty == 3:
		mc.setBlock(pos.x+1, pos.y+2, pos.z, block.STONE.id)
		mc.setBlock(pos.x, pos.y-1, pos.z, block.STONE.id)
		mc.setBlock(pos.x+2, pos.y-1, pos.z, block.STONE.id)
		pos.x += 3
	else:
		if dis == 4 and OPOS.y - pos.y < 4:
			mc.setBlock(pos.x+1, pos.y+2, pos.z, block.STONE.id)
			mc.setBlock(pos.x, pos.y-1, pos.z, block.STONE.id)
			mc.setBlock(pos.x+3, pos.y-2, pos.z, block.STONE.id)
			pos.x += 4
			pos.y -= 1
		else:
			mc.setBlock(pos.x+1, pos.y+2, pos.z, block.STONE.id)
			mc.setBlock(pos.x, pos.y-1, pos.z, block.STONE.id)
			mc.setBlock(pos.x+2, pos.y-1, pos.z, block.STONE.id)
			pos.x += 3

def headhitter(dis):
	if difficulty == 3:
		mc.setBlock(pos.x, pos.y+2, pos.z, block.STONE.id)
		mc.setBlock(pos.x, pos.y-1, pos.z, block.STONE.id)
		mc.setBlock(pos.x+2, pos.y-1, pos.z, block.STONE.id)
		mc.setBlock(pos.x+2, pos.y+2, pos.z, block.STONE.id)
		mc.setBlock(pos.x+3, pos.y-1, pos.z, block.STONE.id)
		pos.x += 4
	else:
		mc.setBlock(pos.x, pos.y+2, pos.z, block.STONE.id)
		mc.setBlock(pos.x, pos.y-1, pos.z, block.STONE.id)
		mc.setBlock(pos.x+dis, pos.y-1, pos.z, block.STONE.id)
		mc.setBlock(pos.x+dis, pos.y+2, pos.z, block.STONE.id)
		mc.setBlock(pos.x+dis+1, pos.y-1, pos.z, block.STONE.id)
		pos.x += dis+2

def neo(dis):
	if difficulty == 5:
		mc.setBlock(pos.x, pos.y-1, pos.z, block.STONE.id)
		mc.setBlock(pos.x+1, pos.y-1, pos.z, block.STONE.id)
		mc.setBlock(pos.x+2, pos.y+1, pos.z, block.STONE.id)
		mc.setBlock(pos.x+3, pos.y-1, pos.z, block.GOLD_BLOCK.id)
		pos.x += 4
	elif difficulty == 6:
		mc.setBlock(pos.x, pos.y-1, pos.z, block.STONE.id)
		mc.setBlock(pos.x+1, pos.y-1, pos.z, block.STONE.id)
		mc.setBlock(pos.x+2, pos.y+1, pos.z, block.STONE.id)
		pos.x += 3
	elif difficulty == 7:
		mc.setBlock(pos.x, pos.y-1, pos.z, block.STONE.id)
		mc.setBlock(pos.x+1, pos.y-1, pos.z, block.STONE.id)
		if dis == 4:
			dis = 3
		for i in range(0,dis):
			mc.setBlock(pos.x+i+2, pos.y+1, pos.z, block.STONE.id)
		mc.setBlock(pos.x+i+3, pos.y-1, pos.z, block.GOLD_BLOCK.id)
		pos.x += i+4
	else:
		mc.setBlock(pos.x, pos.y-1, pos.z, block.STONE.id)
		mc.setBlock(pos.x+1, pos.y-1, pos.z, block.STONE.id)
		if dis == 4:
			dis = 3
		for i in range(0,dis):
			mc.setBlock(pos.x+i+2, pos.y+1, pos.z, block.STONE.id)
		mc.setBlock(pos.x+i+3, pos.y-1, pos.z, block.STONE.id)
		pos.x += i+4

def corner():
	if difficulty == 5:
		mc.setBlock(pos.x, pos.y-1, pos.z, block.STONE.id)
		mc.setBlock(pos.x+1, pos.y+1, pos.z+1, block.STONE.id)
		mc.setBlock(pos.x+2, pos.y-1, pos.z+2, block.GOLD_BLOCK.id)
		pos.x += 3
		pos.z += 3
	elif difficulty == 6:
		mc.setBlock(pos.x, pos.y-1, pos.z, block.STONE.id)
		mc.setBlock(pos.x+1, pos.y+1, pos.z+1, block.STONE.id)
		mc.setBlock(pos.x+2, pos.y-1, pos.z+2, block.STONE.id)
		pos.x += 3
		pos.z += 3
	elif difficulty == 7:
		mc.setBlock(pos.x, pos.y-1, pos.z, block.STONE.id)
		mc.setBlock(pos.x+1, pos.y+1, pos.z+1, block.STONE.id)
		mc.setBlock(pos.x+2, pos.y+1, pos.z+1, block.STONE.id)
		mc.setBlock(pos.x+3, pos.y-1, pos.z+2, block.GOLD_BLOCK.id)
		pos.x += 4
		pos.z += 3
	else:
		mc.setBlock(pos.x, pos.y-1, pos.z, block.STONE.id)
		mc.setBlock(pos.x+1, pos.y+1, pos.z+1, block.STONE.id)
		mc.setBlock(pos.x+2, pos.y+1, pos.z+1, block.STONE.id)
		mc.setBlock(pos.x+3, pos.y-1, pos.z+2, block.STONE.id)
		pos.x += 4
		pos.z += 3
specialjump = 0

# Parkour Course Generation
mc.setBlock(pos.x,pos.y-1,pos.z, block.GOLD_BLOCK.id)
for i in range(25):
	# Parkour Generation Variables
	rng = random.randint(0,50)
	offsetz = 0
	offsety = 0
	dis = random.randint(2,3)
	if difficulty > 0:
		dis = random.randint(3,4)
		if difficulty > 1:
			offsetz = random.randint(0,1)
			offsety = random.randint(0,1)
	
	# Parkour Jump Distance
	pos.x += dis
	
	# The More Difficulty, the More Special Jumps
	def jumprng(chance):
		if rng < 12-chance:
			mc.setBlock(pos.x, pos.y-1 + offsety, pos.z + offsetz, block.GOLD_BLOCK.id)
			specialjump = 0
		elif 10 <= rng <= 10+chance and difficulty > 2:
			skeppy(dis)
			specialjump = 1
		elif 11+chance <= rng <= 11+2*chance and difficulty > 2:
			headhitter(dis)
			specialjump = 1
		elif 12+2*chance <= rng <= 12+2*chance+round(chance/2) and difficulty > 4:
			neo(dis)
			specialjump = 1
		elif 13+2*chance+round(chance/2) <= rng <= 12+2*chance+2*(round(chance/2)) and difficulty > 4:
			corner()
			specialjump = 1
		else:
			mc.setBlock(pos.x, pos.y-1 + offsety, pos.z + offsetz, block.STONE.id)
			specialjump = 0
	
	if difficulty < 5:
		jumprng(2)
	elif 5 <= difficulty <= 6:
		jumprng(3)
	else:
		jumprng(4)
	
	# Adds Extra Block to Impossible 4 Block 1 Up Jump
	if offsety == 1 and dis == 4 and specialjump == 0:
		mc.setBlock(pos.x-1, pos.y-1 + offsety, pos.z + offsetz, block.STONE.id)
	
pos.x += dis
mc.setBlock(pos.x,pos.y-1,pos.z, block.GOLD_BLOCK.id)

# Checkpoint Variables
spos = OPOS
prevspos = spos
# Loop for Checkpoints
while True:
	# Checkpoint On Gold Block
	time.sleep(0.1)
	rpos = mc.player.getTilePos()
	check = mc.getBlock(rpos.x,rpos.y-1,rpos.z)
	if check == block.GOLD_BLOCK: 
		spos = rpos
		if prevspos != spos:
			mc.postToChat("Checkpoint!")
		prevspos = spos
	
	# Return to Last Checkpoint if Fallen
	if rpos.y < OPOS.y - 4:
		mc.player.setTilePos(spos.x,spos.y,spos.z)
		mc.postToChat("You fell! Returing to last checkpoint.")

