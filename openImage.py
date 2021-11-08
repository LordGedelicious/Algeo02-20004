from PIL import Image
import numpy as np
from numpy.core.fromnumeric import shape

def imagePreprocessing(path):
    img = Image.open(path)
    img_mat = np.array(img)

    width = np.size(img_mat, 1)
    length = np.size(img_mat, 0)

    # pisah 4 nilai kedalam matrix berbeda
    red_scale = [[0 for _ in range(width)] for _ in range(length)]
    blue_scale = [[0 for _ in range(width)] for _ in range(length)]
    green_scale = [[0 for _ in range(width)] for _ in range(length)]
    transparency = [[0 for _ in range(width)] for _ in range(length)]

    for i in range(length):
        for j in range(width):
            red_scale[i][j] = img_mat[i][j][0]
            blue_scale[i][j] = img_mat[i][j][1]
            green_scale[i][j] = img_mat[i][j][2]
            transparency[i][j] = img_mat[i][j][3]
    
    # transpose untuk persiapan perkalian
    red_scale_t = np.transpose(red_scale)
    blue_scale_t = np.transpose(blue_scale)
    green_scale_t = np.transpose(green_scale)

    # AAT (A x A^T)
    rrt = mulMatrix(red_scale, red_scale_t)
    bbt = mulMatrix(blue_scale, blue_scale_t)
    ggt = mulMatrix(green_scale, green_scale_t)
    
    # ATA (A^T x A)
    rtr = mulMatrix(red_scale_t, red_scale)
    btb = mulMatrix(blue_scale_t, blue_scale)
    gtg = mulMatrix(green_scale_t, green_scale)


def printMatrix(m):
    for i in range(len(m)):
        for j in range(len(m[0])):
            print(" " * (5-len(str(m[i][j]))), m[i][j], end=" ")
        print()

def mulMatrix(m1, m2):
    m3 = [[0 for _ in range(len(m2[0]))] for _ in range(len(m1))]
    
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m2)):
                m3[i][j] += (int(m1[i][k]) * int(m2[k][j]))
    
    return m3
            

imagePreprocessing("4-3.png")



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
