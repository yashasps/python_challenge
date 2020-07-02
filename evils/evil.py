
from PIL import Image

img=Image.open("evil.jpg")
size=w,h=640,480
new=Image.new('RGB',size)


gfx =open ('evil2.gfx','rb')

x=gfx.read()

#for byte in x:
    #print(int(byte))

#image={}
#for i in range(5):
    #image[i]=open( 'image'+str(i)+'.png' ,'wb' )
b=0
for i in range(0,w,1):
    for j in range(0,h,1):


        if i<=116 and j<=116:
            c = x[b]
            new.putpixel((i,j), (c,c,c,0))
        else:
            new.putpixel((i,j), (0,0,0, 0))
        b+=1
        print(c)


new.save("evil67.jpg")
#for i in range(5):
    #image[i].close()