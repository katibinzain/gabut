import cv2

# Baca gambar asli
image = cv2.imread('gambar.jpg')

# Tampilkan gambar asli
cv2.imshow('Gambar Asli', image)
cv2.waitKey(0)

# Ubah gambar ke dalam skala abu-abu (greyscale)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Tampilkan gambar dalam skala abu-abu
cv2.imshow('Gambar Greyscale', gray_image)
cv2.waitKey(0)

# Ambang batas piksel untuk konversi menjadi gambar biner
threshold = 128

# Konversi gambar greyscale ke gambar biner
_, binary_image = cv2.threshold(gray_image, threshold, 255, cv2.THRESH_BINARY)

# Tampilkan gambar biner
cv2.imshow('Gambar Biner', binary_image)
cv2.waitKey(0)

cv2.destroyAllWindows()
