from PIL import Image
import numpy as np
import svd_process
import time


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
            

def compressMatrix(m_scale, percentage, aat, ata):
    # hitung matriks U,S,V
    u_matrix = np.array(svd_process.singular_vectors(aat, True))
    s_matrix = np.array(svd_process.singular_values(m_scale))
    v_matrix = np.array(svd_process.singular_vectors(ata, False))
    
    # potong matriks sesuai persentase
    k = percentage * rankMatrix(s_matrix) // 100
    u_matrix = u_matrix[:,0:k]
    s_matrix = s_matrix[0:k, 0:k]
    v_matrix = v_matrix[0:k,:]
    
    A = u_matrix @ s_matrix
    A = A @ v_matrix
    
    return A


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
percentage = 100

img = Image.open(path)
img_mat = np.array(img)
length, width, components = img_mat.shape

# pisah 3 nilai kedalam matrix berbeda
red_scale = np.array([[0 for _ in range(width)] for _ in range(length)])
green_scale = np.array([[0 for _ in range(width)] for _ in range(length)])
blue_scale = np.array([[0 for _ in range(width)] for _ in range(length)])

for i in range(length):
    for j in range(width):
        red_scale[i][j] = img_mat[i][j][0]
        green_scale[i][j] = img_mat[i][j][1]
        blue_scale[i][j] = img_mat[i][j][2]

# transpose untuk persiapan perkalian
red_scale_t = np.transpose(red_scale)
green_scale_t = np.transpose(green_scale)
blue_scale_t = np.transpose(blue_scale)

# AAT (A x A^T)
rrt = red_scale @ red_scale_t
ggt = green_scale @ green_scale_t
bbt = blue_scale @ blue_scale_t

# ATA (A^T x A)
rtr = red_scale_t @ red_scale
gtg = green_scale_t @ green_scale
btb = blue_scale_t @ blue_scale

printMatrixInteger(rrt)
print("="*100)
printMatrixInteger(rtr)
print("--- %s seconds ---" % (time.time() - start_time))

# kompresi matriks
red_scale_new = compressMatrix(red_scale, percentage, rrt, rtr)
green_scale_new = compressMatrix(green_scale, percentage, ggt, gtg)
blue_scale_new = compressMatrix(blue_scale, percentage, bbt, btb)

# satukan ketiga matriks
img_mat_new = [[[0 for _ in range(3)] for _ in range(len(red_scale_new[0]))] for _ in range(len(red_scale_new))]
img_new = Image.fromarray(img_mat_new)
img_new.save("compressed_" + path)

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
