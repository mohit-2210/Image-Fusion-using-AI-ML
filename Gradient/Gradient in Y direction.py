import cv2
import numpy as np
import matplotlib.pyplot as plot
import os

#Reading of image
image = cv2.imread("D:\SGP ML-IP\ImagesDataset\IR image\I1.bmp",0)

lap = cv2.Laplacian(image,cv2.CV_64F,ksize=3) 
lap = np.uint8(np.absolute(lap))

# Below code convert image gradient in y direction
sobely= cv2.Sobel(image,0, dx=0,dy=1)
sobely = np.uint8(np.absolute(sobely))

#To save image
path="D:\SGP ML-IP\ImagesDataset\IR Gradient\IY"
cv2.imwrite(os.path.join(path , 'IGY1.jpg'), sobely)

