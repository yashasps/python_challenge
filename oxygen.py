from PIL import Image

img=Image.open("oxygen.png")

y=50
x=0
p=""
for i in range(0,90):

    d=img.getpixel((x,y))[0]
    x+=7

    t=chr(d)
    p+=t

u=[105, 110, 116, 101, 103, 114, 105, 116, 121]

p+="\n"
for i in u:
    p+=chr(i)
print(p)