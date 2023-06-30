import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('c:/Users/AK/Pictures/Saved Pictures/maher3.jfif',0)
citra_grey = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
biner = cv2.threshold(citra_grey, 50, 256, cv2.THRESH_BINARY)[1]

cv2.imshow('gambar', img)
plt.hist(img.ravel(), 50, [0, 256])
plt.show()
print('\n\ngambar\n', img)

cv2.imshow('biner', biner)
plt.hist(biner.ravel(), 50, [0, 256])
plt.show()
print('\n\nbinery\n', biner)

cv2.imshow('citra_grey', citra_grey)
plt.hist(citra_grey.ravel(), 50, [0, 256])
plt.show()
print('\n\ngrey\n', citra_grey)

cv2.waitKey(0)
cv2.destroyAllWindows()