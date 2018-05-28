# -*- coding: utf-8 -*-

# ~ Python: cv2.goodFeaturesToTrack(image, maxCorners, qualityLevel, minDistance[, corners[, mask[, blockSize[, useHarrisDetector[, k]]]]])


# ~ image – Input 8-bit or floating-point 32-bit, single-channel image.
# ~ eig_image – The parameter is ignored.
# ~ temp_image – The parameter is ignored.
# ~ corners – Output vector of detected corners.
# ~ maxCorners – Maximum number of corners to return. If there are more corners than are found, the strongest of them is returned.
# ~ qualityLevel – Parameter characterizing the minimal accepted quality of image corners. The parameter value is multiplied by the best corner quality measure, 
# ~ which is the minimal eigenvalue (see cornerMinEigenVal() ) 
# ~ or the Harris function response (see cornerHarris() ). The corners with the quality measure less than the product are rejected.
# ~ For example, if the best corner has the quality measure = 1500, and the qualityLevel=0.01 , then all the corners with the quality measure less than 15 are rejected.
# ~ minDistance – Minimum possible Euclidean distance between the returned corners.


import numpy as np
import cv2

img = cv2.imread('opencv-corner-detection-sample.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 2)
corners = np.int0(corners)



for corner in corners:
    x,y = corner.ravel()
    cv2.circle(img,(x,y),3,255,-1)
    
cv2.imshow('Corner',img)
cv2.waitKey(0)
cv2.destroyAllWindows


#####other method



# ~ img - Input image, it should be grayscale and float32 type.
# ~ blockSize - It is the size of neighbourhood considered for corner detection
# ~ ksize - Aperture parameter of Sobel derivative used.
# ~ k - Harris detector free parameter in the equation.



# ~ import cv2
# ~ import numpy as np


# ~ img = cv2.imread('opencv-corner-detection-sample.jpg')
# ~ gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# ~ gray = np.float32(gray)

# ~ dst = cv2.cornerHarris(gray,2,3,0.04)

# ~ #result is dilated for marking the corners, not important

# ~ dst = cv2.dilate(dst,None)

# ~ # Threshold for an optimal value, it may vary depending on the image.
# ~ img[dst>0.01*dst.max()]=[0,0,255]


cv2.imshow('dsret',dst)

# ~ cv2.imshow('dst',img)
# ~ cv2.waitKey(0)
# ~ cv2.destroyAllWindows
