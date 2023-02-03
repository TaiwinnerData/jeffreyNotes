import cv2 as cv2
import sys as sys
import numpy as np
#np.set_printoptions(threshold=sys.maxsize)
testImagePath = r"C:\\users\User\Desktop\test.png"
testImage = cv2.imread(testImagePath)
cv2.imshow('testImage', testImage)
#print(testImage)
grayTestImage = cv2.cvtColor(testImage, cv2.COLOR_BGR2GRAY)
cv2.imshow('grayTestImage', grayTestImage)
print(grayTestImage)


cv2.waitKey(0)
cv2.destroyAllWindows()
