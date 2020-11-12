import os, sys
from PIL import Image


# im.size[0] - width, [1] - height
onFrame = False
frames = 0
gifout = []

# depending on incoming arguments, script will do thins differently
if len(sys.argv) == 2:
    imagename = sys.argv[-1]
elif len(sys.argv) == 3:
    imagename = sys.argv[-2]
    frames = int(sys.argv[-1])
im = Image.open(imagename)
width = im.size[0]

if len(sys.argv) == 2:
    # determining number of frames
    for pxY in range(im.size[1]):
        for pxX in range(im.size[0]):
            if pxX == (im.size[0]-1) and onFrame == True:
                onFrame = False
            if im.getpixel((pxX, pxY)) == 255:
                continue
            else:
                if onFrame == False:
                    frames += 1
                    onFrame = True
                    break
                else:
                    break
        if pxX == im.size[0] and onFrame == True:
            onFrame == False

# constructing the .gif
heightdiv = im.size[1]/frames

for i in range(frames):
    box = (0, heightdiv*i, width, heightdiv*i+heightdiv)
    region = im.crop(box)
    gifout.append(region)
    regionname = imagename
    regionname = regionname.split(".")
    regionname = regionname[0]
    #region.save(regionname + str(i) + ".png")
gifout[0].save(regionname + ".gif", save_all=True, append_images=gifout[1:], optimize=False, duration=80, loop=0, disposal=2) # disposal SUPER important