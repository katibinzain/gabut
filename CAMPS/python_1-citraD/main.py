import cv2
import matplotlib.pyplot as plt

gambar = cv2.imread('c:/Users/AK/Pictures/ANIME/images.jfif')
_, biner = cv2.threshold(gambar, 50, 255, cv2.THRESH_BINARY)

cv2.imshow('\nasli\n', gambar)
cv2.imshow('\nbin\n', biner)

plt.hist(biner.ravel(), 256, [0, 256])
plt.show()

print('\n\nasli\n', gambar)
print('\n\nbin\n', biner)

cv2.waitKey(0)
cv2.destroyAllWindows()
