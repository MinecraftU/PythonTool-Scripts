from math import sqrt
from PIL import Image # PIL (pillow) is used for image manipulation

# PythonTools mod imports
import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create() # Get the minecraft world handle

# IMPORTANT: Image to draw's name extention CAN'T be .png (at least on my machine using my python configuration) because pillow's getpixel() function returns 0 when the image has .png
IMAGE_NAME = "garfield.jpg" # Put the image you want here.
IMAGE_SCALEDOWN = 10 # Scale down so image doesn't pass height limit

# Get nessessary data about colored concrete blocks with their rgbs
block_colors = []
with open("block_colors.txt") as f1: # blockcolors.txt has rgba colors
    for line in f1:
        block_colors.append(tuple([int(item) for item in line.strip()[1:-1].split(", ")])) # Converts "string tuple" into real tuple
block_ids = []
with open("block_ids.txt") as f2: # blockids.txt has the concrete ids
    for line in f2:
        block_ids.append(int(line.strip()))

block_matches = {color:bid for (color, bid) in zip(block_colors, block_ids)} # dictionary in form {rgba_color:block_id, ...}

def rgbaColorMatch(color, possible_matches=block_colors):
    """
    Finds the closest rgba match in possible_matches for color

    Apparently the best match is the smallest value described by: 
    d = sqrt( (rimg - rtable)^2 + (gimg - gtable)^2 + (bimg - btable)^2 + (aimg - atable)^2 )
    I found this out on https://www.reddit.com/r/Minecraft/comments/j8s2en/trying_to_find_the_right_blocks_for_specific/
    """

    r, g, b, a = color
    lowest = (1000, (None, None, None, None)) # "lowest" tuple in form (formula_result, rgba_value)
    # Find the lowest result of formula
    for pm in possible_matches:
        d = sqrt((r - pm[0])**2 + (g - pm[1])**2 + (b - pm[2])**2 + (a - pm[3])**2)
        if d < lowest[0]:
            lowest = (d, (pm[0], pm[1], pm[2], pm[3]))
    
    return lowest[1]

pos = mc.player.getTilePos()
large_image = Image.open(IMAGE_NAME)
image = large_image.resize((large_image.size[0] // IMAGE_SCALEDOWN, large_image.size[1] // IMAGE_SCALEDOWN)) # Scale the image down
width, height = image.size
# Place minecraft blocks the same color as pixels on the image to essentially draw the image in minecraft.
for x in range(width):
    for y in range(height):
        pixelrgb = list(image.getpixel((x, y)))
        if len(pixelrgb) == 3: # If image uses RGB mode, not RGBA mode, make it RGBA mode by adding a 255 alpha value
            pixelrgb.append(255)
        pixelrgb = tuple(pixelrgb)
        
        mc.setBlock(pos.x + width - x, pos.y + height - y, pos.z + 10, block.CONCRETE_BLOCK.id, block_matches.get(rgbaColorMatch(pixelrgb))) # pos.x+width-x and pos.y+height-y instead of just pos.x+x and pos.y+y is because first pixel starts on top left of image, not bottom right.
