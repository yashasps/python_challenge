from PIL import Image

img=Image.open('wire.png')


#new=Image.new('RGB',size)

xmin,xmax,ymin,ymax=0,99,0,99
pos=[0,0]
t=0
while ymin!=50 and xmin!=50:
    l=""
    for i in range(xmin,xmax):
        t = t + 1
        pos[0]=i
        v=img.getpixel((t,0))
        print(v)
        #new.putpixel(pos,v)
        l=str(pos[0],"       ",pos[1])
        print(l)
    ymin+=1


    l = ""
    for i in range(0,h):
        t += 1
        pos[1]
        v = img.getpixel((t, 0))
        new.putpixel((w, i), v)

        l = str(w) +"  " + str(  i)
        print(l)

        l = ""
    if t < 9900:
        for i in range(w,j,-1):
            if (i,h) in x:
                break
            v = img.getpixel((t, 0))
            new.putpixel((i,h), v)
            x.append((i,h))
            l = str(i) +"  " + str(  h)
            #print(l)
            t += 1
        l = ""
    if t < 9900:
        for i in range(h,k,-1):
            if (k,i) in x:
                break
            v = img.getpixel((t, 0))
            new.putpixel((k,i), v)
            x.append((k,i))
            l = str(k) +"  " + str(i)
            #print(l)
            t+=1
    j+=1
    k+=1
    h -= 1
    w -= 1
new.save("cats.jpg")
for i in x:
    print(i)
