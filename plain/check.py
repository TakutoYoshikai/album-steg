from stegano import lsb
from stegano import tools
import sys
import struct

def canHide(d, input_image):
    data = tools.binary2base64(d)
    img = tools.open_image(input_image)

    if img.mode not in ["RGB", "RGBA"]:
        if not auto_convert_rgb:
            print("The mode of the image is not RGB. Mode is {}".format(img.mode))
            answer = input("Convert the image to RGB ? [Y / n]\n") or "Y"
            if answer.lower() == "n":
                raise Exception("Not a RGB image.")
        img = img.convert("RGB")
    

    width, height = img.size
    max_bit_size = width * height * 3

    data_length = len(data)
    str_data_length = len(str(data_length))

    data_size = (str_data_length + 1 +data_length)*8

    if(max_bit_size > data_size):
        print("This data can hide")
    else:
        shortage = data_size - max_bit_size
        shortage_size = int(shortage / 3) + 1
        print("Add %d pixel" % shortage_size)
        need_size = data_size / 3 + 1
        print("Need %d pixel" % need_size)