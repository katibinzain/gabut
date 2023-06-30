import cv2
import matplotlib.pyplot as plt

gambar = cv2.imread('c:/Users/AK/Pictures/ANIME/animes.jfif',0)
#gambar_grey = cv2.cvtColor(gambar, cv2.COLOR_BGR2GRAY)
biner = cv2.threshold(gambar, 50, 256, cv2.THRESH_BINARY)[1]

cv2.imshow('bin', biner)
cv2.imshow('asli', gambar)

plt.hist(gambar.ravel(), 150, [0, 256])
plt.show()
print('\n\ngambar\n',gambar)
print('\n\nbinery\n', biner)
cv2.waitKey(0)
cv2.destroyAllWindows()