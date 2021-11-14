from PIL import Image
from math import copysign, sqrt
import numpy as np
from os.path import join, dirname, realpath

import time

def svd(matrix):
    # BIKIN AT*A
    A = matrix.transpose() @ matrix

    # QR ALGORITHM AT*A untuk konvergen mendapatkan eigenvalue A dan eigenvector V
    for i in range(2):
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

    return U, sigma, V


# TO PROCESSS THE DIFFERENT COLOR CHANNELS
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
im1 = Image.open("lol.jpg")
img = np.array(im1)
print(img.shape)


# TIAP CHANNEL
# m = img.shape[0]
# n = img.shape[1]
# red = np.array([[img[i][j][0] for j in range(n)] for i in range(m)]).astype(int)
# green = np.array([[img[i][j][1] for j in range(n)] for i in range(m)]).astype(int)
# blue = np.array([[img[i][j][2] for j in range(n)] for i in range(m)]).astype(int)
# # alpha = np.array([[img[i][j][3] for j in range(n)] for i in range(m)]).astype(int)
# print("UDAH JADI RGB")

# r1, r2, r3 = svd(red)
# r = np.clip(((r1 @ r2) @ r3).round(0), 0, 255)
# print("UDAH R")
# g1, g2, g3 = svd(green)
# g = np.clip(((g1 @ g2) @ g3).round(0), 0, 255)
# print("UDAH G")
# b1, b2, b3 = svd(blue)
# b = np.clip(((b1 @ b2) @ b3).round(0), 0, 255)
# print("UDAH B")

# imgO = np.zeros([m,n,len(img[0][0])])
# # print(imgO)
# imgO[:,:,0] = r
# imgO[:,:,1] = g
# imgO[:,:,2] = b

# imgO = np.uint8(imgO)

# print(img[10])
# print(imgO[10])

imgO = matriximage(img)

imgout = Image.fromarray(imgO)
imgout.save("jancok.jpg", "JPEG")
end = time.time()
print(end-start)