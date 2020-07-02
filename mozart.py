from PIL import Image

img=Image.open("mozart.gif")
size=w,h=640,480
new=Image.new('RGB',(10000,480))

j=[]
for k in range(0,480):
    for i in range(0,w):

        if i <=635:
            if img.getpixel((i,k))==img.getpixel((i+1,k))==img.getpixel((i+2,k))==img.getpixel((i+3,k))==img.getpixel((i+4,k))==195:
                j.append((i-1))
                #x = img.getpixel((i, 0))
                #print(x)
#print(j)

for k in range(0,h):
    for i in range(0,w):
        x = img.getpixel((i, k))
        if i >= j[k]:
            new.putpixel((i - j[k], k), x)
        else:
            if i<=640:
                new.putpixel((j[k] + i, k), x)
new.save("moazrt2.gif")
new.show()

