import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread('image.jpeg',cv2.IMREAD_GRAYSCALE)
# img1=cv2.imread('image.jpeg',cv2.IMREAD_COLOR)
# cv2.imshow('image',img)
# cv2.imshow('image1',img1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
cv2.imwrite('greyscale.png',img)
