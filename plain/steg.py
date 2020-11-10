from stegano import lsb
from stegano import tools
import sys
import struct

def embed(d, img, output):
    data = tools.binary2base64(d)
    secret = lsb.hide(img, data)
    secret.save(output)

def extract(img, output):
    data = tools.base642binary(lsb.reveal(img))
    f = open(output, "wb")
    f.write(data)
    f.close()

