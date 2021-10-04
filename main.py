import os
import sys
from PIL import Image


# im.size[0] - width
# im.size[1] - height
onFrame = False
frames = 0
gifout = []

# depending on incoming arguments, script will do things differently
arg_len = len(sys.argv)
if arg_len == 2:
    # get image name
    imagename = sys.argv[-1]
elif arg_len == 3:
    # get image name and frames
    imagename = sys.argv[-2]
    frames = int(sys.argv[-1])
im = Image.open(imagename)
width = im.size[0]

if arg_len == 2:
    # determining number of frames
    for pxY in range(im.size[1]):
        for pxX in range(im.size[0]):
            
            if pxX == (im.size[0] - 1) and onFrame:
                onFrame = False

            if type(im.getpixel((pxX, pxY))) == tuple:
                if im.getpixel((pxX, pxY))[-1] == 0:
                    continue
                else:
                    if not onFrame:
                        frames += 1
                        onFrame = True
                        break
                    break
                    
            elif type(im.getpixel((pxX, pxY))) == int:
                if im.getpixel((pxX, pxY)) == 255:
                    continue
                else:
                    if not onFrame:
                        frames += 1
                        onFrame = True
                        break
                    break

# constructing the .gif
heightdiv = im.size[1] / frames

for i in range(frames):
    box = (0, heightdiv * i, width, heightdiv * i + heightdiv)
    region = im.crop(box)
    gifout.append(region)
    regionname = imagename
    regionname = regionname.split(".")
    regionname = regionname[0]
   # region.save(regionname + str(i) + ".png")

# disposal SUPER important
gifout[0].save(regionname + ".gif", save_all=True, append_images=gifout[1:], optimize=False, duration=80, loop=0, disposal=2)