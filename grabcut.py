import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('pic.png')

mask = np.zeros(img.shape[:2],np.uint8)

bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)

rect = (51,60,380,500)

cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
img = img*mask2[:,:,np.newaxis]

plt.imshow(img)
plt.colorbar()
plt.show()



# ~ cv2.imshow('img',img)
# ~ cv2.waitKey(0)
# ~ cv2.destroyAllWindows()




# ~ img - Input image
# ~ mask - It is a mask image where we specify which areas are background, foreground or probable background/foreground etc. It is done by the following flags, cv2.GC_BGD, cv2.GC_FGD, cv2.GC_PR_BGD, cv2.GC_PR_FGD, or simply pass 0,1,2,3 to image.
# ~ rect - It is the coordinates of a rectangle which includes the foreground object in the format (x,y,w,h)
# ~ bdgModel, fgdModel - These are arrays used by the algorithm internally. You just create two np.float64 type zero arrays of size (1,65).
# ~ iterCount - Number of iterations the algorithm should run.
# ~ mode - It should be cv2.GC_INIT_WITH_RECT or cv2.GC_INIT_WITH_MASK or combined which decides whether we are drawing rectangle or final touchup strokes.
