import cv2
import numpy as np
import matplotlib.pyplot as plot
import os

#Reading of image
image = cv2.imread("D:\SGP ML-IP\ImagesDataset\IR image\I1.bmp",0)

lap = cv2.Laplacian(image,cv2.CV_64F,ksize=3) 
lap = np.uint8(np.absolute(lap))


# Below code convert image gradient in x direction
sobelx= cv2.Sobel(image,0, dx=1,dy=0)
sobelx= np.uint8(np.absolute(sobelx))


#To save image
path="D:\SGP ML-IP\ImagesDataset\IR Gradient\IX"
cv2.imwrite(os.path.join(path , 'IGX1.jpg'), sobelx)
