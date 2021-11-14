from PIL import Image
from os.path import join

import numpy as np
import time
import svd_qr

def compressor(original_realpath, compressed_realpath, file_name, cprate, prefix):
    start = time.time()
    
    img_in = Image.open(join(original_realpath, file_name))
    
    # Cek mode gambar, jika P atau PA, ubah ke RGB atau RGBA
    im_mode = img_in.mode
    if im_mode == 'P':
        img_in.convert('RGB')
    elif im_mode == 'PA':
        img_in.convert('RGBA')
        
    # Ubah gambar menjadi array
    img_array = np.array(img_in)
    
    # Cek length dan width dari gambar untuk menghitung k
    length, width, _ = img_array.shape
    max_rank = max(length, width)
    k = (cprate * max_rank) // 100

    # Hitung kompresi gambar dengan SVD
    img_compressed = svd_qr.matriximage(img_array, k)

    # Buat kembali gambar dari matriks
    img_out = Image.fromarray(img_compressed, mode=im_mode)
    
    # Jika mode gambar awalnya adalah P atau PA, ubah kembali
    # menjadi P atau PA
    if im_mode == 'P':
        img_out.convert('P')
    elif im_mode == 'PA':
        img_out.convert('PA')
    
    # Save
    img_out.save(join(compressed_realpath, prefix + file_name))
    
    # Hitung runtime
    end = time.time()
    runtime = end - start
    
    # Hitung pixel difference
    pixel_diff = (length * k + k + width * k) / (length * width) * 100

    img_in.close()
    
    return runtime, pixel_diff