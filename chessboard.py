import numpy as np
import cv2 as cv
image = np.full((800, 800, 3),(255,255, 255), dtype=np.uint8)
row,col=0,0

while row<800:
    if (row/100)%2!=1:
        col=100
        while col<800:
            image[row:row+100,col:col+100]=(0,0,0)
            col+=200
    else:
        col=0
        while col<800:
            image[row:row+100,col:col+100]=(0,0,0)
            col+=200
    row+=100
cv.imshow('window',image)
cv.waitKey(0)
cv.destroyAllWindows()
