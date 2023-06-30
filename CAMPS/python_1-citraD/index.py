import cv2
import matplotlib.pyplot as plt

gambar = cv2.imread('c:/Users/AK/Pictures/ANIME/images.jfif')
img_grey = cv2.imread('c:/Users/AK/Pictures/ANIME/images.jfif',0)
#gambar_grey = cv2.cvtColor(gambar, cv2.COLOR_BGR2GRAY)
biner = cv2.threshold(img_grey, 50, 256, cv2.THRESH_BINARY)[1]

cv2.imshow('asli', gambar)
#cv2.imshow('\ngreyscale\n', citra_grey)
cv2.imshow('bin', biner)
cv2.imshow('img_greyscale', img_grey)

plt.hist(gambar.ravel(), 150, [0, 256])
plt.show()

print('\n\ngambar\n', gambar)
print('\n\nimg_greyscale\n', img_grey)
#print('\ngreyscale\n', citra_grey)
print('\n\nbinery\n', biner)

cv2.waitKey(0)
cv2.destroyAllWindows()
