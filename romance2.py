import requests
'''p="12345"
g=""
while True:
    url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing="+str(p)
    r = requests.get(url)
    p=r.text[-5:]
    f=str(r.cookies)

    for i in range(0,len(f)):
        if f[i]=='='and f[i+2]==' ':
            g+=(str(f[i+1]))
            print(g)
        if f[i]=='='and f[i+4]==' ':
            g+=(str(f[i+2])+str(f[i+3]))
            print(g)

import bz2
data=b'BZh91AY26SY943AE2I0000211980P811100AFg9EA000hE3DMB523D0D4D1E28D06A9FA26SD4D321A1EAi7h9B9A2BBF6022C5WXE1ADL80E8V3CC6A8DBH263218A8x0108218DS0BC8AF96KOCA2B0F1BD1DuA0860592sB092C4BcF1w24S850909CAE2490'
print(bz2.compress(data))
#dat=bz2.compress(data)
decompressor=bz2.BZ2Decompressor()
d=decompressor.decompress(data)
print(d)
'''
cook={"info":"the flowers are on their way"}
url='http://www.pythonchallenge.com/pc/stuff/violin.php'
r = requests.get(url,cookies=cook)
print(r.text)