import cv2
import numpy as np

img = cv2.imread('c:/Users/AK/Pictures/Saved Pictures/maher3.jfif')
citra = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

b = img[:,:,0]
g = img[:,:,1]
r = img[:,:,2]

jml_baris =len(citra)
jml_kolom = len(citra[0])

citra_grey = np.zeros((jml_kolom, jml_baris))

for i in range(jml_baris):
    for j in range(jml_kolom):
        citra_grey[i, j] = round(0.299 * r [i, j] + 0.587 * g [i, j] + 0.144 * b [i, j])
    citra_grey = citra_grey.astype(np.uint8)

print('\ncitra', citra)
print('\ncitra_grey', citra_grey)

cv2.imshow('c:/Users/AK/Pictures/Saved Pictures/maher3.jfif',  citra_grey)

cv2.imshow('gambar', img)
cv2.imshow('gambar_2 (greyscale)', citra)
cv2.waitKey(0)