import cv2
import numpy as np

# Membaca gambar dari folder penyimpanan
img = cv2.imread('c:/Users/AK/Pictures/ANIME/animes.jfif')

# Mengubah gambar ke citra grayscale
citra_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

thresh = 127
binaryImg = cv2.threshold(citra_grey, thresh, 255, cv2.THRESH_BINARY)[1]

# Membuat channel matrix dalam gambar
r = img[:,:,0]
g = img[:,:,1]
b = img[:,:,2]

# Menentukan jumlah baris dan kolom citra digital matrix
jml_baris = citra_grey.shape[0]
jml_kolom = citra_grey.shape[1]

# Membuat citra_grey dengan ukuran yang sesuai
citra_grey_new = np.zeros((jml_baris, jml_kolom))

for i in range(jml_baris):
    for j in range(jml_kolom):
        citra_grey_new[i, j] = round(0.299 * r[i, j] + 0.587 * g[i, j] + 0.144 * b[i, j])
citra_grey = citra_grey.astype(np.uint8)

print('\nimg\n', img)
print('\ncitra_grey\n', citra_grey)
print('\nbinary\n', binaryImg)

cv2.imshow('Image', img)
cv2.imshow('Grayscale', citra_grey)
cv2.imshow('Binari', binaryImg)
cv2.waitKey(0)
