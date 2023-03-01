from PIL import Image
import os
temp = 1
def Merge(f1, f2, dir_in1, dir_in2, dir_out):
    #name, ext = os.path.splitext(filename)
    img1 = Image.open(os.path.join(dir_in1, f1))
    img2 = Image.open(os.path.join(dir_in2, f2))
    i1s = img1.size
    i2s = img2.size
    new_image = Image.new('RGB',(i1s[0],2*i2s[1]),(32))
    new_image.paste(img1,(0,0))
    new_image.paste(img2,(0,i1s[0]))
    out = os.path.join(dir_out, "IVGy"+str(temp)+".jpg")
    new_image.save(out)


for i in range(1,5091):
    Merge('IRY'+str(i)+'.jpg','VY'+str(i)+'.jpg',r"D:\SGP ML-IP\Cutted images 32x32\IRY",r"D:\SGP ML-IP\Cutted images 32x32\VY",r"D:\SGP ML-IP\Merge images 32X64\D31")
    temp = temp +1
