import cv2 as cv


img = cv.imread('tiger.jpg')

cv.imshow("Bengal-Tiger", img)

cv.imwrite("new_img.jpg", img)

cv.waitKey(0)
cv.destroyAllWindows()