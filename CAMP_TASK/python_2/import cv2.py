import cv2
import numpy as np

#membaca tempat penyimpanan gambar yang akan ditampilkan
img = cv2.imread('c:/Users/AK/Pictures/PROJECT_CAMPS/animes.jfif')

#melakukan proses perubahan pada gambar yang telah dibaca ke greyscale
thresh = 100
citra_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#menentukan gambar threshold
biner = cv2.threshold(citra_grey, thresh, 255, cv2.THRESH_BINARY)

#matrix gambar yang akan ditampilkan di terminal
b = img[:,:,0]
g = img[:,:,1]
r = img[:,:,2]

#menampilkan baris dan kolom gambar
jml_baris =len(img)
jml_kolom = len(img[0])

#membuat table pengelompokan matrix
citra_grey = np.zeros((jml_kolom, jml_baris))

#menyusun matrix untuk gambar yang akan ditampilkan
for i in range(jml_baris):
    for j in range(jml_kolom):
        citra_grey[i, j] = round(0.299 * r [i, j] + 0.587 * g [i, j] + 0.144 * b [i, j])
citra_grey = citra_grey.astype(np.uint8)

#menampilkan matrix gambar
print(citra_grey)

#menampilkan matrix gambar asli dan gambar yang telah diubah
print('img', img)
print('citra_grey', citra_grey)
print('binery', biner)

#menampilkan dua gambar berbeda atau lebih
cv2.imshow('maher-zain.jfif', img)
cv2.imshow('img_2 (greyscale)', citra_grey)
cv2.waitKey(0)

