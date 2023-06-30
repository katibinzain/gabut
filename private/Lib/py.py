import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('c:/Users/AK/Pictures/Saved Pictures/maher3.jfif', 0)

hist = np.zeros((256,))

for i in img:
    for j in i:
        hist[j] += 1


total_pix = img.shape[0] * img.shape[1]
normal = hist / total_pix

plt.bar(np.arange(256), normal)
plt.xlabel('Intensitas Pixel')
plt.ylabel('Frekuensi normal')
plt.title('Histogram\n')
plt.show()