import cv2

# Membaca gambar
image = cv2.imread('c:/Users/AK/Pictures/ANIME/animes.jfif', cv2.IMREAD_GRAYSCALE)

# Mengubah gambar hitam menjadi putih dan putih menjadi lebih hitam
dark_image = 225 + image

# Menampilkan gambar asli
cv2.imshow('Gambar Asli', image)

# Menampilkan gambar yang telah diubah
cv2.imshow('Gambar Lebih Hitam', dark_image)

# Menunggu hingga tombol apa pun ditekan untuk menutup jendela
cv2.waitKey(0)

# Menghapus semua jendela yang dibuat
cv2.destroyAllWindows()