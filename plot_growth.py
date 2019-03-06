import numpy as np
import matplotlib.pyplot as plt
from os import listdir
import time


src_path = "./imgs_filt/"
dest_path = "./imgs_filt/"

imgs = listdir(src_path)
imgs = sorted(imgs)

# get example picture
#img = plt.imread("./imgs_bk/2019-03-03_0000.jpg")
#img_copy = np.copy(img)

growth = []

for img_path in imgs:


    #start = time.time()
    img = plt.imread(src_path + img_path)
    img_temp = img + [20, 0, 20]
    arr =  np.logical_and( np.logical_and( img_temp[:, :, 0] < img_temp[:, :, 1],  img_temp[:, :, 2]  < img_temp[:, :, 1]), img_temp[:, :, 1] > 100)
    count = np.sum(arr)
    #img_copy[arr] = [255, 0, 0]
    #count = np.sum( img[:, :, 0] < img[:, :, 1] & img[:, :, 2] < img[:,:, 1] & img[:, :, 1] > 180 )
    #end = time.time()

    #print("np time:", (end-start) )
    #print(count)
    growth.append(count)


img_copy = np.copy(img)
img_copy[arr] = [255, 0, 0]

fig, ax = plt.subplots(nrows=2,ncols=1)

#ax[0].imshow(img)
ax[1].imshow(img_copy)
ax[0].plot(growth)
#pylab.savefig('orig.png')
#pylab.clf()
plt.show()
#pylab.savefig('minimal.png' if REDUCED_COLOR_SPACE else 'reduced.png')
