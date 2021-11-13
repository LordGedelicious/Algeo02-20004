from PIL import Image
from os.path import join
import numpy as np
import time
import os

# PIL Save Documentation: https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html


def compressor(original_realpath, compressed_realpath, file_name, cprate, prefix):
    start = time.time()
    
    picture = Image.open(join(original_realpath, file_name))
    pict_as_matrix = np.array(picture)
    
    # inisialisasi
    k = 0
    pict_cp_as_matrix = np.zeros(pict_as_matrix.shape)
    length, width, components = pict_as_matrix.shape
    if components == 3:  # Tiga komponen untuk jpg, yaitu R, G, dan B
        # pisah 3 nilai kedalam matrix berbeda
        red_scale = np.array([[0 for _ in range(width)] for _ in range(length)])
        green_scale = np.array([[0 for _ in range(width)] for _ in range(length)])
        blue_scale = np.array([[0 for _ in range(width)] for _ in range(length)])

        for i in range(length):
            for j in range(width):
                red_scale[i][j] = pict_as_matrix[i][j][0]
                green_scale[i][j] = pict_as_matrix[i][j][1]
                blue_scale[i][j] = pict_as_matrix[i][j][2]
                
        # AAT (A x A^T)
        rrt = red_scale @ red_scale.T
        ggt = green_scale @ green_scale.T
        bbt = blue_scale @ blue_scale.T

        # ATA (A^T x A)
        rtr = red_scale.T @ red_scale
        gtg = green_scale.T @ green_scale
        btb = blue_scale.T @ blue_scale
        
        red_scale_new, k = compress_matrix(red_scale, cprate, rrt, rtr)
        green_scale_new, _ = compress_matrix(green_scale, cprate, ggt, gtg)
        blue_scale_new, _ = compress_matrix(blue_scale, cprate, bbt, btb)
        
        pict_cp_as_matrix[:,:,0] = red_scale_new
        pict_cp_as_matrix[:,:,1] = green_scale_new
        pict_cp_as_matrix[:,:,2] = blue_scale_new
        
        # mengubah semua nilai yang ada menjadi dalam rentang 0 <= val <= 255
        for i, row in enumerate(pict_cp_as_matrix):
            for j, col in enumerate(row):
                for k, value in enumerate(col):
                    if value < 0:
                        pict_cp_as_matrix[i][j][k] = abs(value)
                    if value > 255:
                        pict_cp_as_matrix[i][j][k] = 255
    
    end = time.time()
    runtime = end - start
    
    pict_cp = pict_cp_as_matrix.astype(np.uint8)
    px_diff = (pict_cp.shape[0] * k + k + k * pict_cp.shape[1])/(pict_cp.shape[0] * pict_cp.shape[1]) * 100

    pict_cp = Image.fromarray(pict_cp)
    pict_cp.save(join(compressed_realpath, prefix + file_name))
    picture.close()
    
    return runtime, px_diff

# parameter aat dan ata akan diubah menjadi tidak ada default value = None
# jika fungsi svd sudah jadi
def compress_matrix(m_scale, cprate, aat=None, ata=None):
    # hitung matriks U,S,V
    # u_matrix = svd_process.singular_vectors(aat, True)
    # s_matrix = svd_process.singular_values(m_scale)
    # v_matrix = svd_process.singular_vectors(ata, False)
    
    # kalau fungsi svdnya udah bener, yg ini hapus aja
    u_matrix, s_matrix, v_matrix = np.linalg.svd(m_scale, full_matrices=True)
    s_matrix = np.diag(s_matrix)
    
    #potong matriks sesuai persentase
    k = cprate * np.linalg.matrix_rank(s_matrix) // 100
    u_matrix = u_matrix[:,:k]
    s_matrix = s_matrix[:k, :k]
    v_matrix = v_matrix[:k,:]

    A = np.dot(u_matrix, np.dot(s_matrix, v_matrix))
    
    return A, k