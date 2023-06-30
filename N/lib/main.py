import cv2
import numpy as np

# membaca folder penyimpanan citra_grey
img = cv2.imread('c:/Users/AK/Pictures/PROJECT_CAMPS/animes.jfif')
citra_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

thresh = 127
binaryImg = cv2.threshold(citra_grey, thresh, 255, cv2.THRESH_BINARY)[0]

citra_grey = np.zeros((img))
# membuat channel matrix dalam gambar
r = img[:,:,0]
g = img[:,:,1]
b = img[:,:,2]

#menentukan column citra digital matrix
jml_baris = len(img)
jml_kolom = len(img[0])

citra_grey = np.zeros((jml_kolom, jml_baris))

for i in range(jml_baris):
    for j in range(jml_kolom):
        citra_grey[i, j] = round(0.299 * r [i, j] + 0.587 * g [i, j] + 0.144 * b [i, j])
citra_grey = citra_grey.astype(np.uint8)

print('citra_grey', img)
print('citra_grey', citra_grey)
cv2.imshow('c:/Users/AK/Pictures/ANIME/animes.jfif', img)
#cv2.imshow('citra_grey', img)
cv2.imshow('citra_grey_2 (grayscale)', citra_grey)
cv2.imshow('Citra Abu Abu', binaryImg)
cv2.waitkey(0)