from PIL import Image, ImageDraw, ImageFont

user_color = int(input("Choose what background color you would like:(1-red, 2-green, 3- blue)\n"))
if user_color == 1:
    color = (255, 0, 0)
elif user_color == 2:
    color = (0, 128, 0)
elif user_color == 3:
    color = (0,0,255)
else:
    color = (255, 255, 0)

img = Image.new('RGB', (500, 300), color = color)



d = ImageDraw.Draw(img)

fontPath = "arial.ttf"
fnt = ImageFont.truetype(fontPath, 16)

text_user = input("Please, give some text here:\n")

d.text((30, 250), text_user, font=fnt, fill=(255, 165, 0))

d.polygon([(200,100), (400, 100), (300,240)], fill = (255,255,255))

d.ellipse((250, 100, 350, 200), fill=(0,0,255), outline=(0, 0, 0))



img.save('pil_text.png')
