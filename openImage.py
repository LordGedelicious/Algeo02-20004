import numpy as np
from PIL import Image
import svd_process

img = Image.open("4-3.png")
img_arr = np.array(img)


# 1. Baca Image ***UDAH KELAR***
# 2. Ubah pixel value (RGBA + Grayscale) ke matriks secara terpisah
# 3. Cari perkalian matriks pixel dengan matriks transpose
# 4. Kurangin dengan matriks identitas eigen
# 5. Cari determinan sama dengan nol untuk nomor 4
# 6. Simpen nilai value eigen (harus lebih besar dari nol)
# 7. Cari vektor eigennya (asumsi t = 1 atau disimpan sebagai variabel dl)
# 7.5. Buat matriks U dari normalisasi vektor eigen
# 8. Cari perkalian matriks transpose pixel dengan matriks biasa (singular kanan)
# 9. Cari vektor dan nilai eigen untuk nomor 8
# 10. Buat matriks v
# 11. Buat matriks Sigma dari nilai eigen singular kiri dan kanan (asal bukan nol)
# 12. Ranking matriksnya
# 13. Buat webnya (link ke BE jg)
