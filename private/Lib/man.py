import cv2
import matplotlib.pyplot as plt

img = cv2.imread('c:/Users/AK/Pictures/PROJECT_CAMPS/images (1).jfif')
citra_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, biner = cv2.threshold(citra_grey, 175, 256, cv2.THRESH_BINARY)


plt.hist(img.ravel(), 8, [0, 256])
plt.hist(biner.ravel(), 8, [0, 256])
plt.hist(citra_grey.ravel(), 8, [0, 256])

plt.xlabel('Intensitas Pixel')
plt.ylabel('Frekuensi')
plt.title('HISTOGRAM MATRIX GAMBAR\n')

cv2.imshow('gambar', img)
cv2.imshow('biner', biner)
cv2.imshow('citra_grey', citra_grey)

print('\n\ngmbar\n', img)
print('\n\nbinery\n', biner)
print('\n\ngrey\n', citra_grey)




plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()