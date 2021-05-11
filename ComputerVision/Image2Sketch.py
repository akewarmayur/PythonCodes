

import cv2
img = cv2.imread('IMG-20200803-WA0009.jpg', 3)

# cv2.imshow('gg', img)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# cv2.imshow('ff', img)

img_invert = cv2.bitwise_not(img_gray)

img_smoothing = cv2.GaussianBlur(img_invert, (121, 121),sigmaX=0, sigmaY=0)

def dodgeV2(x, y):

    return cv2.divide(x, 255 - y, scale=256)

final_img = dodgeV2(img_gray, img_smoothing)

cv2.imshow('ff', final_img)
cv2.imwrite('anu2.png', final_img)
cv2.waitKey(0)