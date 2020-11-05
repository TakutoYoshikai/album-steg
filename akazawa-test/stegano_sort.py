from stegano import lsb
import random
import os

# python側で弄ってからライブラリに投げ込むテスト
# 入れる文字列
text = "Hello stegano world"

# default
path = "./default"
files = os.listdir(path)
file = [f for f in files if os.path.isfile(os.path.join(path, f))]
random.shuffle(file)
print(file)

length = len(text)
next = 0

# いい感じのパターンを創り出す（遅い） 
while True:
    # 文字列と同じ長さの順列ができるまで繰り返しているのでなんとかしたい
    word_len =  random.choices(range(length), k=len(file))

    if sum(word_len) == length:
        break

print(word_len)

for count, (fname, wlen) in enumerate(zip(file, word_len)):
    write = str(count) + text[next:next+wlen]
    print(write)
    secret = lsb.hide("./default/" + fname,write)
    secret.save("./output/" + fname)
    next += wlen


# 復元してみる
read = []

output_file = [f for f in files if os.path.isfile(os.path.join(path, f))]
for j in output_file:
    print(lsb.reveal("./output/" + j))
    read.append(lsb.reveal("./output/" + j))

sort = sorted(read)
print(sort)

rebuild = ""
for k in sort:
    rebuild = rebuild + k[1:]

print(rebuild)


# secret = lsb.hide("./default/1.png","Hello test world")

# secret.save("./output/1.png")
# print(lsb.reveal("./output/1.png"))