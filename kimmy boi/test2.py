import cv2 

img = cv2.imread('dbd.jpg',0)

_, img = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

cv2.imwrite('test2.jpg',img)
