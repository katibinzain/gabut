import cv2
import matplotlib.pyplot as plt

gambar = cv2.imread('c:/Users/AK/Pictures/ANIME/animes.jfif')
gambar_grey = cv2.cvtColor(gambar, cv2.COLOR_BGR2GRAY)
_, binery = cv2.threshold(gambar, 50, 256, cv2.THRESH_BINARY)

cv2.imshow('gambar', gambar)
cv2.imshow('gambar_grey', gambar_grey)
cv2.imshow('binery', binery)

plt.figure(figsize=(8, 6))

# Histogram
plt.subplot(2, 1, 1)
plt.hist(binery.ravel(), 150, [0, 256])
plt.xlabel('Nilai Piksel')
plt.ylabel('Frekuensi')
plt.title('Histogram Gambar Asli')

# Plot matriks binery
plt.subplot(2, 1, 2)
plt.imshow(binery, cmap='gray')
plt.xlabel('Kolom')
plt.ylabel('Baris')
plt.title('Gambar binery')

plt.tight_layout()
plt.show()

print('\n\nGambar:\n', gambar)
print('\n\nbineryy:\n', binery)

cv2.waitKey(0)
cv2.destroyAllWindows()
