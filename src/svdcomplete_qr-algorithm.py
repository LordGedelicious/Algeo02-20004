from PIL import Image
import numpy as np
from os.path import join, dirname, realpath

import time

def svd(matrix):
    # BIKIN AT*A
    A = matrix.transpose() @ matrix

    # QR ALGORITHM AT*A untuk konvergen mendapatkan eigenvalue A dan eigenvector V
    for i in range(1):
        # DIGUNAKAN BUILT-IN FUNGSI QR DECOMPOSITION, asumsi boleh karena tidak langsung menghasilkan SVD
        Q, R = np.linalg.qr(A)
        A = R @ Q
        if not i:   # iterasi pertama inisialisasi V dengan Q
            V = Q
        else:
            V = V @ Q   # iterasi selanjutnya V = Q1 * Q2 ... * QN

    # DAPATKAN SIGMA
    sigma = np.diag(np.sqrt(np.absolute(np.diagonal(A))))

    # Hitung inv(sigma) untuk menemukan U
    invsigma = np.linalg.inv(sigma)

    # U dari U = A * V * inv(S),  dapat asumsi V^T^-1 = V karena V orthogonal
    U = (matrix @ V) @ invsigma

    # TRANSPOSE V
    V = np.transpose(V)

    print(U.shape, sigma.shape, V.shape)
    return U, sigma, V


# TO PROCESSS THE DIFFERENT COLOR CHANNELS
# SUPPORT L, LA, RGB, RGBA, CMYK
def matriximage(colormatrix):
    m = colormatrix.shape[0]
    n = colormatrix.shape[1]
    col_channels = colormatrix.shape[2]

    imgO = np.zeros([m,n,col_channels])

    if col_channels > 0:
        c1 = np.array([[colormatrix[i][j][0] for j in range(n)] for i in range(m)]).astype(int)
        c11, c12, c13 = svd(c1)
        c1_f = np.clip(((c11 @ c12) @ c13).round(0), 0, 255)
        imgO[:,:,0] = c1_f
    if col_channels > 1:
        c2 = np.array([[colormatrix[i][j][1] for j in range(n)] for i in range(m)]).astype(int)
        c21, c22, c23 = svd(c2)
        c2_f = np.clip(((c21 @ c22) @ c23).round(0), 0, 255)
        imgO[:,:,1] = c2_f
    if col_channels > 2:
        c3 = np.array([[colormatrix[i][j][2] for j in range(n)] for i in range(m)]).astype(int)
        c31, c32, c33 = svd(c3)
        c3_f = np.clip(((c31 @ c32) @ c33).round(0), 0, 255)
        imgO[:,:,2] = c3_f
    if col_channels > 3:
        c4 = np.array([[colormatrix[i][j][3] for j in range(n)] for i in range(m)]).astype(int)
        c41, c42, c43 = svd(c4)
        c4_f = np.clip(((c41 @ c42) @ c43).round(0), 0, 255)
        imgO[:,:,3] = c4_f

    return np.uint8(imgO)


start = time.time()
im1 = Image.open("input.jpg")
# CEK MODE GAMBAR
print(im1.mode)
img = np.array(im1)
# CEK ROW, WIDTH, COLOR_CHANNELS DARI GAMBAR
print(img.shape)

# HITUNG KOMPRESI DENGAN SVD
imgO = matriximage(img)

# BUAT KEMBALI GAMBAR DARI MATRIX
imgout = Image.fromarray(imgO, mode=im1.mode)

# SAVE
imgout.save("output.jpg")
end = time.time()

# RUNTIME
print(end-start)