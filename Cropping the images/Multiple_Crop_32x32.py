
from PIL import Image
from itertools import product
import os
temp=1
def tile(filename, dir_in, dir_out, d, c):
    name, ext = os.path.splitext(filename)
    img = Image.open(os.path.join(dir_in, filename))
    w, h = img.size
    grid = product(range(0, h-h%d, d), range(0, w-w%d, d))
    for i, j in grid:
        box = (j, i, j+d, i+d)
        fname = "VX" + str(c) +".jpg"
        c = c+1
        temp = c

        out = os.path.join(dir_out, fname)
        img.crop(box).save(out)
    return c
        

for i in range(1,19):
    temp = tile('VGX'+str(i)+'.jpg',r"D:\SGP ML-IP\ImagesDataset\Visual Gradient\VX",r'D:\SGP ML-IP\Cutted images 32x32\VX',32,temp)

