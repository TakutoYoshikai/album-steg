from PIL import Image
import os


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



def reveral(imagepath):
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
    f = open("output", "wb")
    f.write(d)
    f.close()
                

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
            if index + 3 <= len_binary:
                pixel = image.getpixel((col, row))
                r = pixel[0]
                g = pixel[1]
                b = pixel[2]
                r = setlsb(r, binary[index])
                g = setlsb(g, binary[index + 1])
                b = setlsb(b, binary[index + 2])
                if image.mode == "RGBA":
                    encoded.putpixel((col, row), (r, g, b, pixel[3]))
                else:
                    encoded.putpixel((col, row), (r, g, b))
                index += 3
            else:
                image.close()
                return encoded



reveral("hello.png")
#hide("takuto-meshi.png", "/home/lucky/obin/hw").save("hello.png")
