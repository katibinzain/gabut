import cv2
import matplotlib.pyplot as plt 
import numpy as np


img = cv2.imread('CAMP_TASK/python06/mlbb.jpg',0)
# citra_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, biner = cv2.threshold(img, 70, 255, cv2.THRESH_BINARY)


print('gambar', img)
# print('\n\nGAMBAR GRESCALE:\n', citra_grey)
print('biner', biner)

cv2.imshow('gambar', img)
# cv2.imshow('\n\nGAMBAR GRESCALE:\n', citra_grey)
cv2.imshow('biner', biner)


max = np.array([255, 203, 228, 215,  168, 158, 146, 198, 201, 220,  
                154, 144, 131, 212, 181, 211, 159, 149, 136, 159, 223, 230,  
                251, 245, 242, 155, 220, 228,  255, 251, 248, 154, 219, 228, 255, 251,  249])
ig, ax = plt.subplots(figsize =(10, 1))
ax.hist(max, bins = [ 150, 160, 165, 170, 180, 225 ,240, 256 ])


# Show plot
plt.show()
cv2.waitKey(0)