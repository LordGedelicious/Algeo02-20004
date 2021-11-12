from PIL import Image
from os.path import join

# PIL Save Documentation: https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html


def compressor(original_realpath, compressed_realpath, file_name, cprate, prefix):
    picture = Image.open(join(original_realpath, file_name))

    picture.save(join(compressed_realpath, prefix+file_name),quality=cprate) 
    picture.close()