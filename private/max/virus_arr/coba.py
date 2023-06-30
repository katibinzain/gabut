import cv2
import numpy as np

citra = cv2.imread('c:/Users/AK/Pictures/PROJECT_CAMPS/animes.jfif')
citra_grey = cv2.cvtColor(citra, cv2.COLOR_BGR2GRAY)

#menampilkan matrix dari citra
b = citra[:,:,0]
g = citra[:,:,1]
r = citra[:,:,2]

jml_baris = len(citra) 
jml_kolom = len(citra[0]) 

citr_grey = np.zeros((jml_baris, jml_kolom))

for i in range(jml_baris):
    for j in range(jml_kolom):
        citra_grey[i, j] = round(0.299 * r [i, j] + 0.587 * g [i, j] + 144 * b [i, j])
citra_grey = citra_grey.astype(np.uint8)

cv2.imshow("animes",citra_grey)

print(citra_grey)

cv2.waitKey(0)