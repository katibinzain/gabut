import cv2
import matplotlib.pyplot as plt

img = cv2.imread('c:/Users/AK/Pictures/PROJECT_CAMPS/anime.jfif')
citra_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, biner = cv2.threshold(img, 75, 255, cv2.THRESH_BINARY)

print('biner', biner)
print('asli', img)
print('Greyscale', citra_grey)

cv2.imshow('biner', biner)
cv2.imshow('asli', img)
cv2.imshow('greyscale', citra_grey)

plt.hist(img.ravel(), 256, [0, 256])
plt.hist(biner.ravel(), 276, [0, 276])
plt.hist(citra_grey.ravel(), 156, [0, 256])
plt.title('Histogram\n')
plt.show()
print(img)

cv2.waitKey(0)
cv2.destroyAllWindows()