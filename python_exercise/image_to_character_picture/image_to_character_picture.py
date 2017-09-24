from PIL import Image
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('file') # 输入文件
parser.add_argument('-o', '--output')   # 输出文件
parser.add_argument('--width', type=int, default=80)    # 字符画宽，默认为80
parser.add_argument('--height', type=int, default=80)   # 字符画高，默认为80

args = parser.parse_args()

IMG = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output

# 字符画所使用的字符集，一共70个字符
ascii_char = list(
    "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

def get_char(r, g, b, alpha=256):
    # 白色用空白代替
    if(alpha == 0):
        return ' '

    length = len(ascii_char)
    # 这一行灰度的变化是为什么？
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    unit = (256.0 + 1) / length
    return ascii_char[int(gray/unit)]

if(__name__ == '__main__'):
    image = Image.open(IMG)
    image = image.resize((WIDTH, HEIGHT), Image.NEAREST)

    txt = ''

    print(image.getpixel((20, 30)))

    for i in range(HEIGHT):
        for j in range(WIDTH):
            # 在调用函数时，使用单星号可以解压参数列表
            # image.getpixel会返回对应文件的不同通道参数。png文件具有(R, G, B, Alpha)四个通道
            txt += get_char(*image.getpixel((j, i)))
        txt += '\n'

    print(txt)

    # 字符画输出到文件
    if(OUTPUT):
        with open(OUTPUT, 'w') as f:
            f.write(txt)
    else:
        with open('output.txt', 'w') as f:
            f.write(txt)