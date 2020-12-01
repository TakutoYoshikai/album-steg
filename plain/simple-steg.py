from PIL import Image
import os
from functools import reduce


def list_images(dr):
    imagenames = list(filter(lambda x: x.endswith(".png"), os.listdir(dr)))
    images = []
    for imagename in imagenames:
        imagepath = dr + "/" + imagename
        images.append(Image.open(imagepath))
    return images

def capacity_of_images(images):
    result = 0
    for image in images:
        result += capacity_of_image(image)
    return result


def message_to_binary(message):
    if type(message) == str:
        return ''.join([ format(ord(i), "08b") for i in message])
    elif type(message) == bytes:
        return [ format(i, "08b") for i in message ]
    elif type(message) == bytearray:
        return [ format(i, "08b") for i in bytes(message) ]
    elif type(message) == int:
        return format(message, "08b")

def setlsb(component, bit):
    return component & ~1 | int(bit)

def getbit(c):
    return c & 1

def split(binary):
    index = 0
    n_array = []
    while index < len(binary):
        if len(binary) - index < 8:
            break
        byte = ""
        for i in range(0, 8):
            byte += binary[index + i]
        n = int(byte, 2)
        n_array.append(n)
        index += 8
    return bytearray(bytes(n_array))

def cut_bytes(data):
    delimeter = "#|#|#|#".encode()
    delimeter = bytearray(delimeter)
    print(len(delimeter))
    j = 0
    for i in range(len(data)):
        if data[i] == delimeter[j]:
            j = j + 1
        else:
            j = 0
        if j >= len(delimeter):
            return data[:i - len(delimeter) + 1]
    return data



def reveral(imagepath, filepath):
    image = Image.open(imagepath)
    width, height = image.size
    binary = ""
    for row in range(height):
        for col in range(width):
            pixel = image.getpixel((col, row))
            if image.mode == "RGBA":
                pixel = pixel[:3]
            for color in pixel:
                binary += str(getbit(color))
    d = bytes(cut_bytes(split(binary)))
    f = open(filepath, "wb")
    f.write(d)
    f.close()
                
def capacity_of_image(image):
    width, height = image.size
    del_len = len(bytearray("#|#|#|#".encode()))
    return (width * height * 3 - del_len) // 8

def hide(imagepath, filepath):
    image = Image.open(imagepath)
    if image.mode not in ["RGB", "RGBA"]:
        image = image.convert("RGB")
    encoded = image.copy()
    width, height = image.size
    n_bytes = width * height * 3 // 8
    file_bytes = os.path.getsize(filepath)
    delimeter = "#|#|#|#".encode()
    delimeter = bytearray(delimeter)
    if file_bytes + len(delimeter) > n_bytes:
        raise ValueError("file size is too large")
    index = 0
    f = open(filepath, "rb")
    content = f.read()
    content = bytearray(content)
    content.extend(delimeter)
    binary_content = message_to_binary(content)

    binary = "".join(binary_content)
    len_binary = len(binary)
    for row in range(height):
        for col in range(width):
            if index < len_binary:
                pixel = image.getpixel((col, row))
                r = pixel[0]
                g = pixel[1]
                b = pixel[2]
                r = setlsb(r, binary[index])
                if index + 1 < len_binary:
                    g = setlsb(g, binary[index + 1])
                if index + 2 < len_binary:
                    b = setlsb(b, binary[index + 2])
                if image.mode == "RGBA":
                    encoded.putpixel((col, row), (r, g, b, pixel[3]))
                else:
                    encoded.putpixel((col, row), (r, g, b))
                index += 3
            else:
                image.close()
                return encoded


print(capacity_of_images(list_images("images")))
