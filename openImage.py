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

    printMatrix(red_scale)
    print("\n")

    # transpose untuk persiapan perkalian
    red_scale_t = np.transpose(red_scale)
    blue_scale_t = np.transpose(blue_scale)
    green_scale_t = np.transpose(green_scale)

    printMatrix(red_scale_t)
    print("\n")

    # AAT (A x A^T)
    rrt = np.matmul(red_scale, red_scale_t)
    bbt = np.matmul(blue_scale, blue_scale_t)
    ggt = np.matmul(green_scale, green_scale_t)

    print(rrt[0][0])
    printMatrix(rrt)

    # ATA (A^T x A)
    rtr = np.matmul(red_scale_t, red_scale)
    btb = np.matmul(blue_scale_t, blue_scale)
    gtg = np.matmul(green_scale_t, green_scale)



def printMatrix(m):
    for i in range(len(m)):
        for j in range(len(m[0])):
            if (len(str(m[i][j])) == 3):
                print(m[i][j], end=" ")
            elif (len(str(m[i][j])) == 2):
                print("", m[i][j], end=" ")
            else:
                print(" ", m[i][j], end=" ")
        print()

imagePreprocessing("4-3.png")

