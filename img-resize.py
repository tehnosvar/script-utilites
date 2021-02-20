#!/usr/bin/env python3

from PIL import Image, UnidentifiedImageError
import os

text_file = open('text.txt', 'w')
list_files = os.listdir(path=".")
id = 0

for image in list_files:
    id += 1
    try:
        img = Image.open(image)
        width = 640
        height = 480
        res_img = img.resize((width, height), Image.ANTIALIAS)
        res_img.save(image)
        text_file.write(str(img.size)+ " .... "  + image + '\n')
    except UnidentifiedImageError:
        pass
    except IsADirectoryError:
        pass
    

text_file.close()
