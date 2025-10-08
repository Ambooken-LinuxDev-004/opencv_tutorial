import cv2 as cv


img1 = cv.imread('hot-air-ballon.jpg', 0)

cv.imshow("Hot Air Ballon", img1)

cv.waitKey(0)
cv.destroyAllWindows()
