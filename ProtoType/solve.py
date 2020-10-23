import os
from PIL import Image
 
path = "./AFPicture"
files = os.listdir(path)
file = [f for f in files if os.path.isfile(os.path.join(path, f))]

for name in file:    
    img = Image.open('AFPicture/'+name)
    rgba_img = img.convert('RGBA')
    size = rgba_img.size
    
    flag = False
    cnt = 0
    for y in range(size[1]):
        for x in range(size[0]):
    
            r,g,b,a = rgba_img.getpixel((x,y))
            r = r % 3
            g = g % 4
            b = b % 5
            if r == 0:
                print(" ", end="")
            elif r == 1:
                if g == 0:
                    if b == 0:
                        print(" ", end="")
                    elif b == 1:
                        print(".", end="")
                    elif b == 2:
                        print("?", end="")
                    elif b == 3:
                        print("0", end="")
                    elif b == 4:
                        print("1", end="")
                if g == 1:
                    if b == 0:
                        print("2", end="")
                    elif b == 1:
                        print("3", end="")
                    elif b == 2:
                        print("4", end="")
                    elif b == 3:
                        print("5", end="")
                    elif b == 4:
                        print("6", end="")
                if g == 2:
                    if b == 0:
                        print("7", end="")
                    elif b == 1:
                        print("8", end="")
                    elif b == 2:
                        print("9", end="")
                    elif b == 3:
                        print("a", end="")
                    elif b == 4:
                        print("b", end="")
                if g == 3:
                    if b == 0:
                        print("c", end="")
                    elif b == 1:
                        print("d", end="")
                    elif b == 2:
                        print("e", end="")
                    elif b == 3:
                        print("f", end="")
                    elif b == 4:
                        print("g", end="")
            elif r == 2:
                if g == 0:
                    if b == 0:
                        print("h", end="")
                    elif b == 1:
                        print("i", end="")
                    elif b == 2:
                        print("j", end="")
                    elif b == 3:
                        print("k", end="")
                    elif b == 4:
                        print("l", end="")
                if g == 1:
                    if b == 0:
                        print("m", end="")
                    elif b == 1:
                        print("n", end="")
                    elif b == 2:
                        print("o", end="")
                    elif b == 3:
                        print("p", end="")
                    elif b == 4:
                        print("q", end="")
                if g == 2:
                    if b == 0:
                        print("r", end="")
                    elif b == 1:
                        print("s", end="")
                    elif b == 2:
                        print("t", end="")
                    elif b == 3:
                        print("u", end="")
                    elif b == 4:
                        print("v", end="")
                if g == 3:
                    if b == 0:
                        print("w", end="")
                    elif b == 1:
                        print("x", end="")
                    elif b == 2:
                        print("y", end="")
                    elif b == 3:
                        print("z", end="")
                    elif b == 4:
                        pass
    
            #終了処理
            if r == 2 and g == 3 and b == 4:
                flag = True
                print(" ")
                break
        if flag:
            break