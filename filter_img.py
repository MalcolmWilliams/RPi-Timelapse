from os import listdir
from PIL import Image
from PIL import ImageStat
from shutil import copy
import matplotlib.pyplot as plt

src_path = "./imgs_raw/"
dest_path = "./imgs_filt/"

brightness_tol = 25

imgs = listdir(src_path)
imgs = sorted(imgs)

def brightness( im_file ):
   im = Image.open(im_file).convert('L')
   stat = ImageStat.Stat(im)
   return stat.mean[0]

brightness_arr = []
for i in range(len(imgs)):
    brightness_arr.append(brightness(src_path + imgs[i]))
    if(brightness_arr[-1] > brightness_tol):
        copy(src_path + imgs[i], dest_path) 

plt.plot(brightness_arr)
plt.show()
