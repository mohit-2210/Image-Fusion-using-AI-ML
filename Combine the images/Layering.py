import cv2
import numpy as np
import os
temp = 1

def Data(f1, i1, f2, i2, f3, i3):
    img1 = cv2.imread(os.path.join(i1,f1))
    img2 = cv2.imread(os.path.join(i2,f2))
    img3 = cv2.imread(os.path.join(i3,f3))


    dst = cv2.addWeighted(img1, 1, img2, 1, 0)
    dst1 = cv2.addWeighted(dst, 1, img3, 1, 0)
    img_arr = np.hstack((img1, img2))

    path = "D:\SGP ML-IP\Final Dataset\VI dataset-2"
    cv2.imwrite(os.path.join(path ,"VI "+str(temp)+".jpg"), dst1)
    

for i in range(1,5091):
    Data("M"+str(i)+".jpg",r'D:\SGP ML-IP\Merge images 32X64\VI',"VIGx"+str(i)+".jpg",'D:\SGP ML-IP\Merge images 32X64\D22',"VIGy"+str(i)+".jpg","D:\SGP ML-IP\Merge images 32X64\D32")
    temp = temp +1
