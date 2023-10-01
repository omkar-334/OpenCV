import cv2 as cv
img=cv.imread('trial.jpg')
print(img.shape)
crop=img[60:120,80:160]
cv.imshow('mycroppedimage',crop)
cv.waitKey(0)
cv.destroyAllWindows()
cv.imwrite('crop.jpg',crop)