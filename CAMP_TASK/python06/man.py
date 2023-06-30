import cv2
import matplotlib.pyplot as plt

img = cv2.imread("c:/Users/AK/Pictures/ANIME/animes.jfif",0)
citra_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, biner = cv2.threshold(citra_grey, 50, 256, cv2.THRESH_BINARY)

cv2.imshow("gambar", img)
cv2.imshow("gambar(greyscale)", citra_grey)
cv2.imshow("gambar(binery)", biner)

plt.figure(figsize=(8, 6))

plt.subplot(2, 1, 1)
plt.hist(citra_grey.ravel(), 150, [0, 256])
plt.xlabel("Nilai Pixel")
plt.ylabel("Frekuensi")
plt.title("HISTOGRAM GAMBAR")

plt.subplot(2, 1, 2)
plt.imshow(biner, cmap='grey')
plt.xlabel("Kolom")
plt.ylabel("Baris")
plt.title("Gambar Binery")

plt.tight_layout()
plt.show()

print("\n\nGAMBAR:\n", img)
print("\n\nBINERY\n", biner)

cv2.waitKey(0)
cv2.destroyAllWindows()