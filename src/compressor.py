from PIL import Image
import PIL
import os
import glob
from os.path import join, dirname, realpath

file_name = "sudah submisi.PNG"
picture = Image.open(join(dirname(realpath(__file__)), file_name))
print(f"The image size dimensions are: {picture.size}")


print(join(dirname(realpath(__file__)), file_name))
picture.save(join(dirname(realpath(__file__)), "compressed_"+file_name),optimize=True,quality=30) 