from PIL import Image
import numpy as np
from numpy.core.fromnumeric import shape
import svd_process
import time


def mulMatrix(m1, m2):
    m3 = [[0 for _ in range(len(m2[0]))] for _ in range(len(m1))]
    
    p = 0
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m2)):
                m3[i][j] += (int(m1[i][k]) * int(m2[k][j]))
    return m3


def rankMatrix(m):
    """ Fungsi mengembalikan rank dari matriks.
    
        Prekondisi: baris nol matriks berada di paling bawah."""
        
    length, width = m.shape
    rank = 0
    i = 0
    lanjut = True
    while i < length and lanjut:
        zero_count = 0
        for j in range(width):
            if m[i,j] == 0:
                zero_count += 1
        
        if zero_count == width:
            lanjut = False
        else:
            rank += 1
            i += 1
    
    return rank
            

# def compressMatrix(m, percentage):
#     k = percentage * rankMatrix(s_matrix) // 100
    
#     # potong matriks
#     u_matrix = u_matrix


def printMatrixInteger(m):
    for i in range(len(m)):
        for j in range(len(m[0])):
            if (len(str(m[i][j])) == 1):
                print("    ", m[i][j], end=" ")
            elif (len(str(m[i][j])) == 2):
                print("   ", m[i][j], end=" ")
            elif (len(str(m[i][j])) == 3):
                print("  ", m[i][j], end=" ")
            elif (len(str(m[i][j])) == 4):
                print(" ", m[i][j], end=" ")
            elif (len(str(m[i][j])) == 5):
                print("", m[i][j], end=" ")
            else:
                print(m[i][j], end=" ")
                
        print()
            

# imagePreprocessing("4-3.png")
# sample = np.array([[10, 0, 2], [0, 10, 4], [0, 0, 1]])
# print(rankMatrix(sample))

# ASUMSI FORMAT GAMBAR JPEG (TIDAK ADA NILAI TRANSPARANSI)
start_time = time.time()

path = "4-3.png"
img = Image.open(path)
img_mat = np.array(img)
print(img_mat.shape)
width = np.size(img_mat, 1)
length = np.size(img_mat, 0)

# pisah 4 nilai kedalam matrix berbeda
red_scale = [[0 for _ in range(width)] for _ in range(length)]
blue_scale = [[0 for _ in range(width)] for _ in range(length)]
green_scale = [[0 for _ in range(width)] for _ in range(length)]

for i in range(length):
    for j in range(width):
        red_scale[i][j] = img_mat[i][j][0]
        blue_scale[i][j] = img_mat[i][j][1]
        green_scale[i][j] = img_mat[i][j][2]

printMatrixInteger(red_scale)
# transpose untuk persiapan perkalian
red_scale_t = np.transpose(red_scale)
blue_scale_t = np.transpose(blue_scale)
green_scale_t = np.transpose(green_scale)
print("="*100)
printMatrixInteger(red_scale_t)

# AAT (A x A^T)
rrt = np.array(mulMatrix(red_scale, red_scale_t))
bbt = np.array(mulMatrix(blue_scale, blue_scale_t))
ggt = np.array(mulMatrix(green_scale, green_scale_t))
print("="*100)
printMatrixInteger(rrt)

# ATA (A^T x A)
rtr = np.array(mulMatrix(red_scale_t, red_scale))
btb = np.array(mulMatrix(blue_scale_t, blue_scale))
gtg = np.array(mulMatrix(green_scale_t, green_scale))

# hitung matriks U,S,V
u_r_matrix = svd_process.singular_vectors(rrt, True)
s_r_matrix = svd_process.singular_values(red_scale)
v_r_matrix = svd_process.singular_vectors(rtr, False)

print(u_r_matrix)
print("="*100)
print(s_r_matrix)
print("="*100)
print(v_r_matrix)

print("--- %s seconds ---" % (time.time() - start_time))

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
