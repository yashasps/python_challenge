from PIL import Image

img=Image.open("cave.jpg")
size=w,h=640,480
new=Image.new('RGB',size)

for x in range(0,w,2):
    for y in range(0,h,2):
        even=img.getpixel((x,y))
        odd =img.getpixel((x+1, y+1))
        new.putpixel((x,y),even)
        new.putpixel((x+1,y+1),odd)

new.save("cave2.jpg")
new.show()