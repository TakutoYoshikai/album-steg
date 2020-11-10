import sys
import os
from PIL import Image
 
#画像に隠蔽するテキスト
f = open('text.txt', 'r')
sys.stdin = f
txt = list(input())
 
#画像
path = "./Picture"
files = os.listdir(path)
file = [f for f in files if os.path.isfile(os.path.join(path, f))]


#print(file)
#len(file)
parse=len(txt)//len(file)+1

justcnt=0
for name in file:
    img = Image.open('Picture/'+name)
    rgba_img = img.convert('RGBA')
    size = rgba_img.size
    result = Image.new('RGBA',size)
    result.paste(rgba_img, (0, 0))
    
    flag = False
    cnt = 0
    for y in range(size[1]):
        for x in range(size[0]):
    
            r,g,b,a = rgba_img.getpixel((x,y))
            r = r // 3 * 3
            g = g // 4 * 4
            b = b // 5 * 5
            
            if justcnt >= len(txt):
                break
            get_ord = ord(txt[justcnt])
            if flag:
                get_ord = ord('!')
            #R
            # 空白 . ? 数字 a ~ g
            if get_ord == 32 or get_ord == 46 or get_ord == 63 \
                or (get_ord >= 48 and get_ord <= 57) \
                or (get_ord >= 97 and get_ord <= 103):
                r += 1
            # h ~ z or end(!)
            elif (get_ord >= 104 and get_ord <= 122) or get_ord == 33:
                r += 2
    
            #G
            # 2 ~ 6 m ~ q
            if (get_ord >= 50 and get_ord <= 54) \
                or (get_ord >= 109 and get_ord <= 113):
                g += 1
            # 7 ~ 9 a ~ b r ~ v
            elif (get_ord >= 55 and get_ord <= 57) \
                or get_ord == 97 or get_ord == 98 \
                or (get_ord >= 114 and get_ord <= 118):
                g += 2
            # c ~ g w ~ z
            elif (get_ord >= 99 and get_ord <= 103) \
                or (get_ord >= 119 and get_ord <= 122) \
                or get_ord == 33:
                g += 3
    
            #B
            if r % 3 == 1:
                # .
                if get_ord == 46: b += 1
                # ?
                elif get_ord == 63:b += 2
                # 数字
                elif (get_ord >= 48 and get_ord <= 57):
                    b += (get_ord - 45) % 5
                # a ~ g
                elif (get_ord >= 97 and get_ord <= 103):
                    b += (get_ord - 94) % 5
            elif r % 3 == 2:
                # h ~ z
                if get_ord >= 104 and get_ord <= 122:
                    b += (get_ord - 104) % 5
                # end(!)
                elif  get_ord == 33:
                    b += 4
    
            result.putpixel((x,y),(r,g,b,a))
            if flag:
                break
            if cnt < parse - 1:
                cnt += 1
                justcnt+= 1
            #終了処理
            if cnt == parse - 1 or (r % 3 == 2 and g % 4 == 3 and b % 5 == 4):
                flag = True
        if flag:
            break
    result.save('AFPicture/'+name)