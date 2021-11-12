from PIL import Image
from os.path import join


def compressor(original_realpath, compressed_realpath, file_name, cprate, prefix):
    picture = Image.open(join(original_realpath, file_name))

    picture.save(join(compressed_realpath, prefix+file_name),optimize=True,quality=cprate) 
    picture.close()