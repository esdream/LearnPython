from PIL import Image, ImageFont, ImageDraw

def add_num(image):
    img = Image.open(image)
    width, height = img.size
    font = ImageFont.truetype('arial.ttf', 100)

    draw = ImageDraw.Draw(img)
    draw.text((4*width/5, height/6), '5', (255, 0, 0), font=font)
    draw = ImageDraw.Draw(img)

    img.save('head_num.png')

if(__name__ == '__main__'):
    add_num('head.png')